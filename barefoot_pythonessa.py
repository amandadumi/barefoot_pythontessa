import webbrowser
import sys

###############################################################################
###############################################################################
###############################################################################
recipes={'entree':
{
'gnocchi':['https://food52.com/recipes/70772-instant-potato-gnocchi','No additional notes'],
'white-bean gnocchi' : ['http://sweetpeasandsaffron.com/2015/10/pan-fried-gnocchi-with-sundried-tomatoes-and-white-beans.html','No additional notes'],
'mac & cheese':['http://carlsbadcravings.com/million-dollar-macaroni-cheese-casserole-recipe/','No additional notes'],
},
'dessert':{'creme brulee' : ['https://foodal.com/recipes/desserts/how-to-make-a-simple-creme-brulee/','No additional notes']},
'breakfast':{'crepes':['https://www.sweetashoney.co/french-crepes-recipe-easy/','No additional notes']},
}
###############################################################################
###############################################################################
###############################################################################

def get_cat(recipes):
    j=sorted(recipes)
    print('Please input # from the following options:')
    for idx,key in enumerate(j):
        print('{idx}: {key}'.format(idx=idx+1,key=key))
    print('\nTo exit, type x')
    try:
        number = input('-->')
        if number != 'x':
            number = j[int(number)-1]
    except:
        number = None

    if number == 'x':
        exit()
    elif (number not in recipes.keys()):
        print('Try again')
        return get_cat(recipes)
    else:
        return number

def get_rec(cat):
    j=sorted(cat)
    print('\nSelect a recipe # from the following:')
    for idx,key in enumerate(j):
        print('{idx}: {key}'.format(idx=idx+1,key=key))
    print('\nTo exit type x')
    try:
        rec = input('-->')
        if rec != 'x':
            rec = j[int(rec)-1]
    except:
        rec = None

    print(rec)
    if rec == 'x':
        sys.exit()
    elif rec not in cat.keys():
        print('Try again')
        return get_rec(cat)
    else:
        return rec

def actions(recipes):
    cat=get_cat(recipes)
    cat = recipes['{}'.format(cat)]
    rec=get_rec(cat)
    recipe=cat['{}'.format(rec)]
    return webbrowser.open_new('{}'.format(recipe[0]))


actions(recipes)
