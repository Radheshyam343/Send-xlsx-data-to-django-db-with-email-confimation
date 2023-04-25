import pandas as pd
from core.models import Menu
from django.core.management.base import BaseCommand

# Read the Excel file into a pandas DataFrame
class Command(BaseCommand):
    help = 'Imports menu data from an XLSX file'
    def handle(file):
        try:
            df = pd.read_excel(file)
            df.columns = df.columns.str.lower()

            # Iterate over the rows in the DataFrame and create Menu and Ingredient instances
            for row in df.iterrows():
                # Extract the data for the Menu model fields
                pdf_number = row['pdf number']
                recipe_name = row['recipe name']
                alternate_name = row['alternate name']
                recipe_type = row['recipe type']
                description = row['description']
                meat_type = row['meat type']
                meat_classification = row['meat classification']
                cuisine = row['cuisine']
                serving_quantity = row['serving quantity']
                serve = row['serve']
                meal_type = row['meal type']
                cookware = row['cookware']
                calories_per_serving = row['calories per\nserving']
                actual = row['actual']
                alternate = row['alternate']
                comments = row['comments']
                oz = row['oz']
                ml = row['ml']
                pound = row['pound']
                kg = row['kg']
                gm = row['gm']
                cubes = row['cubes']
                pints = row['pints']
                tbsp = row['tbsp']
                lb = row['lb']
                tsp = row['tsp']
                cm = row['cm']
                cups = row['cups']
                inch = row['inch']
                bowl = row['bowl']
                pinch = row['pinch']
                litres = row['litres']
                count = row['count']
                cakes = row['cakes']
                piece = row['piece']
                squares = row['squares']
                stalks = row['stalks']
                variation_alternate = row['variation / alternate']
                dsp = row['dsp']
                slices = row['slices']
                flakes = row['flakes']
                bunch = row['bunch']
                cubes_2 = row['cubes']
                whole_heads = row['whole heads']
                for_taste = row['for taste']
                part = row['part']
                heaped_tsp = row['heaped tsp']
                catty = row['catty']
                cooking = row['cooking']
                pre_cooking = row['pre- cooking']
                cook_tip = row['cook tip']
                serve_tip = row['serve tip']
                others = row['others']
                cook_time = row['cook time']
                prep_time = row['prep time']
                soak_time = row['soak time']
                marinate_time = row['marinate time']
                total_time = row['total_time']
                energy = row['energy']
                protein = row['protein']
                kcal = row['kcal']
                cal = row['cal']
                carbohydrate = row['carbohydrate']
                sugars = row['sugars']

                # Create a new Menu instance and save it to the database
                menu = Menu(
                    pdf_number = pdf_number,
                    recipe_name = recipe_name,
                    alternate_name = alternate_name,
                    recipe_type = recipe_type,
                    description = description,
                    meat_type = meat_type,
                    meat_classification = meat_classification,
                    cuisine = cuisine,                
                    serving_quantity = serving_quantity,
                    serve = serve,
                    meal_type = meal_type,
                    cookware = cookware,
                    calories_per_serving = calories_per_serving,
                    actual = actual,
                    alternate = alternate,
                    comments = comments,
                    oz =oz,
                    ml =ml,
                    pound = pound,
                    kg = kg,
                    gm = gm,
                    cubes = cubes,
                    pints = pints,
                    tbsp = tbsp,
                    lb  = lb,
                    tsp = tsp,
                    cm  = cm,
                    cups = cups,
                    inch = inch,
                    bowl = bowl,
                    pinch = pinch,
                    litres = litres,
                    count = count,
                    cakes = cakes,
                    piece = piece,
                    squares = squares,
                    stalks = stalks,
                    variation_alternate = variation_alternate,
                    dsp = dsp,
                    slices = slices,
                    flakes =flakes,
                    bunch = bunch,
                    cubes_2 = cubes_2,
                    whole_heads = whole_heads,
                    for_taste =for_taste,
                    part = part,
                    heaped_tsp =heaped_tsp,
                    catty = catty,
                    cooking =cooking,
                    pre_cooking = pre_cooking,
                    cook_tip = cook_tip,
                    serve_tip = serve_tip,
                    others = others,
                    cook_time = cook_time,
                    prep_time = prep_time,
                    soak_time = soak_time,
                    marinate_time =marinate_time,
                    total_time = total_time,
                    energy = energy,
                    protein =protein,
                    kcal = kcal,
                    cal = cal,
                    carbohydrate = carbohydrate,
                    sugars = sugars,
                    )
                menu.save()
            return True

        except Exception as e:
            return False

                
