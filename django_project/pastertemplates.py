from paste.script.templates import Template


class DjangoProjectTemplate(Template):
    summary = 'Django project template'
    vars = []
    use_cheetah = True
    _template_dir = 'project_template'
