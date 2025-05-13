from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

# В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. 
# Каждому продукту может соответствовать несколько категорий или ни одной. 
# А каждой категории может соответствовать несколько продуктов или ни одного. 
# Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта 
# – Имя категории» и имена всех продуктов, у которых нет категорий.

def get_product_category_pairs(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_links_df: DataFrame
) -> DataFrame:
    """
    Возвращает датафрейм со всеми парами "Продукт-Категория" и продуктами без категорий
    """
    # Соединяем продукты с их категориями через таблицу связей
    products_with_categories = (
        products_df.join(
            product_category_links_df,
            on="product_id",
            how="left"
        )
        .join(
            categories_df,
            on="category_id",
            how="left"
        )
        .select(
            col("product_name"),
            col("category_name")
        )
    )
    
    # Отдельно получаем продукты без категорий
    products_without_categories = (
        products_df.join(
            product_category_links_df,
            on="product_id",
            how="left_anti"
        )
        .select(
            col("product_name"),
            lit(None).alias("category_name")
        )
    )
    
    # Объединяем оба результата
    result = products_with_categories.union(products_without_categories)
    
    return result
