foods = {"apple": "130","avocado": "50","banana": "110","cantaloupe": "50","grapefruit": "60","grapes": "90","honeydew melon": "50","kiwifruit": "90","lemon": "15","lime": "20","nectarine": "60","orange": "80","peach": "60","pear": "100","pineapple": "50","plums": "70","strawberries": "50","sweet cherries": "100","tangerine": "50","watermelon": "80",
         "asparagus": "20","bell pepper": "25","broccoli": "45","carrot": "30","cauliflower": "15","celery": "10","cucumber": "10","green (snap) beans": "20","green cabbage": "25","green onion": "10","iceberg lettuce": "10","leaf lettuce": "15","mushrooms": "20","onion": "45","potato": "110","radishes": "20","summer squash": "20","sweet corn": "90","sweet potato": "100",
         "blue crab": "100","catfish": "130","clams": "110","cod": "90","flounder/sole": "100","haddock": "100","halibut": "120","lobster": "80","ocean perch": "110","orange roughy": "80","oysters": "100","pollock": "90","rainbow trout": "140","rockfish": "110","salmon, atlantic/coho/sockeye/chinook": "200","salmon, chum/pink": "130","scallops": "140","shrimp": "100","swordfish": "120","tilapia": "110","tuna": "130"
         }


item = input("Item: ").lower()
if item in foods:
    print("Calories:", foods[item])
