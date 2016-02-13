import layout

module_head = '<div class="col-lg-4 col-md-6 col-sm-12">'
module_foot = '</div>'

label_head = '<span class="label">'
label_foot = '</span>'

container_head = '<div class="row">'
container_foot = '</div>'

percentage_bar = '<div class="progress"><div class="progress-bar" style="width: {}%"></div></div>'

value = '<p> {} </p>'

def htmlForDisplay(module, recur=False):
    if not recur:
        builder = module_head
    else:
        builder = container_head
    for element in module.getLayout():
        if isinstance(element, Label):
            builder += label_head
            builder += element.getText()
            buidler += label_foot
        elif isinstance(element, PercentBar):
            builder += percentage_bar.format(element.getPercentage())
        elif isinstance(element, Value):
            builder += value.format(element.getValue())
        elif isinstance(element, Container):
            builder += htmlForDisplay(element, True)
    if not recur:
        builder += module_foot
    else:
        builder += container_foot
    return builder

