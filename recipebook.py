# Recipe Book with Ingredient Checker

# Pre-loaded recipes with ingredients
recipes = {
    "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "baking powder"],
    "spaghetti bolognese": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "olive oil"],
    "omelette": ["eggs", "milk", "salt", "pepper", "cheese"],
    "salad": ["lettuce", "tomato", "cucumber", "olive oil", "salt", "pepper"],
}

# Store user's pantry as a set of available ingredients
pantry = set()

# Function to add a new recipe
def add_recipe():
    recipe_name = input("\nEnter the recipe name: ").strip()
    ingredients = input("Enter ingredients (comma-separated): ").strip().split(',')
    ingredients = [ingredient.strip().lower() for ingredient in ingredients]
    
    recipes[recipe_name.lower()] = ingredients
    print(f"Recipe for '{recipe_name}' added successfully.")

# Function to view all recipes
def view_recipes():
    if not recipes:
        print("\nNo recipes added yet.")
        return
    
    print("\nRecipes:")
    for recipe, ingredients in recipes.items():
        print(f"- {recipe.title()}: {', '.join(ingredients)}")

# Function to add ingredients to pantry
def add_to_pantry():
    new_ingredients = input("\nEnter ingredients to add to your pantry (comma-separated): ").strip().split(',')
    new_ingredients = [ingredient.strip().lower() for ingredient in new_ingredients]
    
    pantry.update(new_ingredients)
    print(f"Ingredients '{', '.join(new_ingredients)}' added to pantry.")

# Function to check if a recipe can be made
def check_recipe():
    recipe_name = input("\nEnter the name of the recipe you want to check: ").strip().lower()
    
    if recipe_name not in recipes:
        print(f"No recipe found with the name '{recipe_name}'.")
        return
    
    recipe_ingredients = set(recipes[recipe_name])
    missing_ingredients = recipe_ingredients - pantry
    
    if not missing_ingredients:
        print(f"You have all the ingredients to make '{recipe_name.title()}'.")
    else:
        print(f"You're missing these ingredients to make '{recipe_name.title()}': {', '.join(missing_ingredients)}")

# Function to view pantry contents
def view_pantry():
    if not pantry:
        print("\nYour pantry is empty.")
    else:
        print(f"\nYour pantry contains: {', '.join(pantry)}")

# Main function to run the recipe book
def recipe_book():
    while True:
        print("\nRecipe Book Menu")
        print("1. Add a Recipe")
        print("2. View All Recipes")
        print("3. Add Ingredients to Pantry")
        print("4. View Pantry")
        print("5. Check if You Can Make a Recipe")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "3":
            add_to_pantry()
        elif choice == "4":
            view_pantry()
        elif choice == "5":
            check_recipe()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
1
# Run the recipe book app
if __name__ == "__main__":
    recipe_book()
