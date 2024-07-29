# test-task-itguru
Выполнение этого тестового задания https://docs.google.com/document/d/1CHrWQUmUeglX0vvFQaQExysVRA12hDzg/edit?usp=drive_link&amp;ouid=116465374620540440947&amp;rtpof=true&amp;sd=true

Даталогическая схема данных:
![](https://github.com/rublock/test-task-itguru/raw/main/static/img/erd.png)

Получение информации о сумме товаров заказанных под каждого клиента (Наименование клиента, сумма):
```sql
SELECT
    mainapp_client.name,
    SUM(mainapp_orderitem.quantity * mainapp_product.price) AS total_quantity -- Сумма стоимости всех товаров, заказанных клиентом
FROM
    mainapp_orderitem
JOIN
    mainapp_client ON mainapp_orderitem.client_id = mainapp_client.id -- Объединяем с таблицей клиентов
JOIN
    mainapp_product ON mainapp_orderitem.product_id = mainapp_product.id -- Объединяем с таблицей продуктов
GROUP BY
    mainapp_client.id, mainapp_client.name
ORDER BY
    mainapp_client.name ASC;
```