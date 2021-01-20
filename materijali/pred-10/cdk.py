from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_rds as rds,
    aws_secretsmanager as secretsmanager,
    core,
)


class WebAppStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, database_name: str='cloud', webapp_min_capacity: int=1, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # setup a dedicated Virtual Private Cloud (VPC) for this entire stack
        vpc = ec2.Vpc(scope=self, id='vpc')

        # setup an auto scaling serverless Aurora/PostgreSQL database cluster
        database_cluster = rds.ServerlessCluster(
            scope=self,
            id='database',
            vpc=vpc,
            engine=rds.DatabaseClusterEngine.aurora_postgres(
                # HACK: as per AWS console only PostgreSQL 10.7 and 10.12 serverless db engine versions are supported
                version=rds.AuroraPostgresEngineVersion.VER_10_12,
            ),
            default_database_name=database_name, # auto-create the database with this name
            scaling=rds.ServerlessScalingOptions(
                auto_pause=core.Duration.minutes(10), # pause the database after 10 minutes of idle time
                min_capacity=rds.AuroraCapacityUnit.ACU_2,
                max_capacity=rds.AuroraCapacityUnit.ACU_16,
            )
        )

        # webapp, a serverless Fargate service running on an ECS cluster and fronted by an application load balancer
        webapp_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            scope=self,
            id='webapp',
            vpc=vpc,
            cpu=256, # 0.25 vCPU
            memory_limit_mib=512, # 0.5 GB RAM
            desired_count=webapp_min_capacity, # desired Fargate task capacity
            task_image_options={
                'image': ecs.ContainerImage.from_asset(directory='.'), # build Docker image in-situ, directly from Dockerfile
                'container_port': 8000,
                'environment': {
                    # security
                    'DEBUG': 'false',

                    # database
                    'DB_NAME': database_name,
                    'DB_HOST': core.Token.as_string(database_cluster.cluster_endpoint.hostname),
                    'DB_PORT': core.Token.as_string(database_cluster.cluster_endpoint.port),
                },
                'secrets': {
                    # security
                    'SECRET_KEY': ecs.Secret.from_secrets_manager(secretsmanager.Secret(scope=self, id='DJANGO_SECRET_KEY')),

                    # database
                    'DB_USER': ecs.Secret.from_secrets_manager(database_cluster.secret, 'username'),
                    'DB_PASS': ecs.Secret.from_secrets_manager(database_cluster.secret, 'password'),
                },
            },
        )

        # allow webapp service to access the database cluster
        database_cluster.connections.allow_default_port_from(webapp_service.service)

        # setup webapp service auto scaling
        webapp_service_auto_scaler = webapp_service.service.auto_scale_task_count(
            min_capacity=webapp_min_capacity,
            max_capacity=30,
        )
        webapp_service_auto_scaler.scale_on_cpu_utilization(
            id='cpu-scaling',
            target_utilization_percent=75, # target CPU utilization across *all* tasks in this service
        )


def get_cdk_app():
    app = core.App()

    WebAppStack(app, 'cloud-computing')

    return app

def main():
    get_cdk_app().synth()

if __name__ == '__main__':
    main()
