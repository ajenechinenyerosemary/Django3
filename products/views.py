from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Products

# Create your views here.

@csrf_exempt
def getProducts(request):
  if request.method == 'GET':
    product= Products.objects.all()

    product_list = list(product.values())
    return JsonResponse({
      "message": "Get product route is active",
       "data" : product_list  })
  else:
    return JsonResponse({"message": "invalid method"},status=405)
  
@csrf_exempt
def add_product(request):
  if request.method =="POST":
      # model syntax for adding products
      json_data = request.body .decode("utf-8")
      data_dict = json.loads(json_data)
    #Extract the product name from the data
      product_name = data_dict.get("name")
    #check if a product with the given name already exists
      existing_product = Products.objects.filter(name = product_name).first()
      if existing_product:
          #if the product exists, return a message indicating so
        return JsonResponse({"message": "Product with this name already"},status = 400 )
      else:
        Products.objects.create(**data_dict)
        return JsonResponse({
      "message": "post added successfully" })
  else:
   
   return JsonResponse({"message": "invalid method"},status=405)

#Another method
# Product.objects.create(
    #  name = "Apple watch series 8",
    #  image_url ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-tWHO4-G0PnaueR8HfDyeQcBulNI-Lt5pdw&s",
    #  description ="A cool watch worth its price",
    #  type ="smartwatch",
     # brand ="Apple",
     # price = 400000,
     # available = True

   # )
   #method 1
    # Product.objects.create(
    #  name = data_dict["name"],
    #  image_url = data_dict["image_url"],
    #  description = data_dict["description"],
    #  type = data_dict["type"],
    #  brand = data_dict["brand"],
     # price = data_dict["price"],
     # available = data_dict["available"]

     #ASSIGNMENT
    
@csrf_exempt
def edit_product(request):
    if request.method =="PUT":
        json_data = request.body .decode("utf-8")
        data_dict = json.loads(json_data)
        product_id = data_dict.get("product_id")
        if product_id:
            try:
                      product = Products.objects.get(id=product_id)
            except Products.DoesNotExist: 
                  return JsonResponse({"message": "Product not found"}, status=404)
              
            if "name" in data_dict:
                    product.name = data_dict["name"]
            if "image_url" in data_dict:
                      product.image_url = data_dict["image_url"]
            if "description" in data_dict:
                      product.description = data_dict["description"]
            if "type" in data_dict:
                      product.type = data_dict["type"]
            if "brand" in data_dict:
                      product.brand = data_dict["brand"]
            if "price" in data_dict:
                      product.price = data_dict["price"]
            if "available" in data_dict:
                      product.available = data_dict["available"] 
            product.save()

        return JsonResponse({"message": "Product updated successfully"}, status=200)
    else:
        return JsonResponse({"message":"invalid method"}, status=405)

@csrf_exempt
def delete_product(request):
    if request.method == "DELETE":
        json_data = request.body .decode("utf-8")
        data_dict = json.loads(json_data)
        product_id = data_dict.get("product_id")
        try:
            product = Products.objects.get(id=product_id)
            product.delete()
            return JsonResponse({}, status=204) 
        except Products.DoesNotExist:
            return JsonResponse({"message": "Product not found"}, status=404)
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)