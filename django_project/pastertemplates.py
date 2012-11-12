from paste.script.templates import Template


class DjangoProjectTemplate(Template):
    vars = []
    use_cheetah = True
    _template_dir = 'project_template'
