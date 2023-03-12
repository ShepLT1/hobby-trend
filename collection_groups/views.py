# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Product, Variant
# # from .serializers import ProductSerializer, VariantSerializer
# from .models import Product
# import uuid
# from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator

# class ProductsView(APIView):
#     def get(self, request, page=1, limit=50, format=None):
#         """
#         Return a list of all products.
#         """
#         if request.GET.get("page"):
#             page = int(request.GET.get("page"))

#         if request.GET.get("limit"):
#             limit = int(request.GET.get("limit"))

#         products = Product.objects.all()
#         paginator = Paginator(products, limit)
#         page_result = paginator.get_page(page)

#         # serializer = ProductSerializer(page_result.object_list, many=True)

#         return Response(
#             {
#                 "count": products.count(),
#                 "data": serializer.data,
#                 "page": page,
#                 "limit": limit,
#             },
#             status=status.HTTP_200_OK,
#         )


# class ProductView(APIView):
#     def get(self, request, product_id: uuid, format=None):
#         """
#         Return details for a single product
#         """

#         product = get_object_or_404(Product, id=product_id)
#         serializer = ProductSerializer(product)

#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK,
#         )

#     def put(self, request, product_id: uuid, format=None):
#         product = get_object_or_404(Product, id=product_id)

#         serializer = ProductSerializer(
#             instance=product, data=request.data, partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class VariantView(APIView):
#     def get(self, request, variant_id: uuid, format=None):
#         """
#         Return details for a single product
#         """

#         variant = get_object_or_404(Variant, id=variant_id)
#         serializer = VariantSerializer(variant)

#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK,
#         )

#     def put(self, request, variant_id: uuid, format=None):
#         variant = get_object_or_404(Variant, id=variant_id)

#         serializer = VariantSerializer(
#             instance=variant, data=request.data, partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
