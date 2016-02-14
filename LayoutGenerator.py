from layout import Label
from layout import Container
from layout import Value
from layout import PercentBar
module_head = '<div class="col-lg-4 col-md-6 col-sm-12">'
module_foot = '</div>'

module_label = '<h2>{}</h2>'

label_head = '<p>'
label_foot = '</p>'

container_head = '<div class="row">'
container_foot = '</div>'

percentage_bar = '<div class="progress"><div class="progress-bar" style="width: {}%"></div></div>'

value = '<p> {} </p>'

def htmlForDisplay(module, recur=False):
    if not recur:
        builder = module_head
        builder += module_label.format(module.getName())
    else:
        builder = container_head
    print (module)
    for element in module.getLayout():
        if isinstance(element, Label.Label):
            builder += label_head
            builder += element.getText()
            builder += label_foot
        elif isinstance(element, PercentBar.PercentBar):
            builder += percentage_bar.format(element.getPercentage())
        elif isinstance(element, Value.Value):
            builder += value.format(element.getValue())
        elif isinstance(element, Container.Container):
            builder += htmlForDisplay(element, True)
    if not recur:
        builder += module_foot
    else:
        builder += container_foot
    return builder

