import click

from jsub import Jsub

from jsub.config  import load_config_file

class Run(object):
    def __init__(self, jsubrc, task_profile_file, dry_run):
        self.__jsubrc = jsubrc
        self.__task_profile_file = task_profile_file
        self.__dry_run = dry_run

    def execute(self):
        j = Jsub(self.__jsubrc)
        task_profile = load_config_file(self.__task_profile_file)
        task = j.create(task_profile)
        j.submit(task, dry_run=self.__dry_run)

        click.echo('Task submitted successfully')
        click.echo('- ID         : %s' % task.data['id'])
        click.echo('- Name       : %s' % task.data['name'])
        click.echo('- Job Number : %s' % len(task.data['jobvar']))
