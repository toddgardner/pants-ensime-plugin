from pants.goal.task_registrar import TaskRegistrar as task
from ensime.pants.tasks.ensime_gen import EnsimeGen

def register_goals():
  task(name='ensime', action=EnsimeGen).install(replace=True)
