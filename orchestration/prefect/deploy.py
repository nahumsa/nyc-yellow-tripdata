from prefect.deployments import DeploymentSpec
from prefect.flow_runners import SubprocessFlowRunner
from prefect.orion.schemas.schedules import CronSchedule

from orchestration.prefect.train_lr import train_and_valid_lr

DeploymentSpec(
    flow=train_and_valid_lr,
    parameters={"year": 2022, "month": 1},
    name="nyc-yellow-taxi",
    schedule=CronSchedule(cron="0 0 1 * *"),
    flow_runner=SubprocessFlowRunner(),
    tags=["ml"],
)
