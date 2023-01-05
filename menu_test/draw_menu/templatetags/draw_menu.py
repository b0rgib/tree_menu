from django import template
from draw_menu.models import Item


register = template.Library()


@register.inclusion_tag('draw_menu/menu.html', takes_context=True)
def draw_menu(context, menu):
    items = Item.objects.filter(menu__name=menu)
    items_values = list(items.values())
    primary_item = [item for item in list(filter(lambda item: item['parent_id'] == None, items_values))]
    for item in primary_item:
        item['child_items'] = []
        item['path'] = str(item['id'])
    try:
        path_to_selected = list(context['request'].GET[menu].split('-'))
        path = ''
        for i in range(len(path_to_selected)):
            cur = list(filter(lambda item: item['id'] == int(path_to_selected[i]), items_values))[0]
            if path == '':
                path = str(cur['id'])
            else:
                path = path + '-' + str(cur['id'])
            cur['path'] = path
            if i == len(path_to_selected) - 1:
                cur['child_items'] = list(filter(lambda item: item['parent_id'] == cur['id'], items_values))
                for item in cur['child_items']:
                    item['path'] = path + '-' + str(item['id'])
            else:
                cur['child_items'] = [list(filter(lambda item: item['id'] == int(path_to_selected[i+1]), items_values))[0]]
    except:
        pass
    result_dict = {'items': primary_item}
    result_dict['menu'] = menu
    result_dict['other_querystring'] = get_querystring(context, menu)
    return result_dict


def get_querystring(context, menu):
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = ('&').join(querystring_args)
    return querystring