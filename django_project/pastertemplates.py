from os import getlogin, path
from socket import gethostname
from datetime import datetime

from paste.script.templates import Template, var


class DjangoProjectTemplate(Template):
    summary = 'Django project template'
    use_cheetah = True
    _template_dir = 'project_template'
    vars = (
            var('username', 'Enter your name',
                default=getlogin()),
            var('email_address', 'Enter your email address',
                default='{}@{}'.format(getlogin(), gethostname())),
            )

    def run(self, command, output_dir, vars):
        now = datetime.now()
        vars['creation_date'] = now.strftime('%Y-%m-%d %H:%M:%S.%f Z')
        super(DjangoProjectTemplate, self).run(command, output_dir, vars)
        self.write_ditz_config(output_dir, vars)


    def write_ditz_config(self, output_dir, vars):
        config_path = path.join(output_dir, '.ditz-config')
        config = ('--- !ditz.rubyforge.org,2008-03-06/config\n'
                'name: {username}\n'
                'email: {email_address}\n'
                'issue_dir: bugs')
        config = config.format(
                username=vars['username'],
                email_address=vars['email_address'],
                )
        with open(config_path, 'w') as config_file:
            config_file.write(config)
