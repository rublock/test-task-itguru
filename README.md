# test-task-itguru
Выполнение этого тестового задания https://docs.google.com/document/d/1CHrWQUmUeglX0vvFQaQExysVRA12hDzg/edit?usp=drive_link&amp;ouid=116465374620540440947&amp;rtpof=true&amp;sd=true

Даталогическая схема данных:
![](https://github.com/rublock/test-task-itguru/raw/main/static/img/erd.png)

Получение информации о сумме товаров заказанных под каждого клиента (Наименование клиента, сумма):
```sql
SELECT
    mc.name,
    SUM(mo.quantity * mp.price) AS total_quan
FROM
    mainapp_orderitem AS mo
INNER JOIN
    mainapp_client AS mc
ON 
    mo.client_id = mc.id
INNER JOIN
    mainapp_product AS mp
ON 
    mo.product_id = mp.id
GROUP BY
    mc.id, mc.name
ORDER BY
    mc.name ASC;
```
Найти количество дочерних элементов первого уровня вложенности для категорий номенклатуры:
```sql
SELECT
    mc.name,
    COUNT(mp.parent_id) AS reference_count
FROM
    mainapp_category AS mc
LEFT JOIN
    mainapp_category AS mp ON mc.id = mp.parent_id
GROUP BY
    mc.id, mc.name
ORDER BY
    reference_count DESC;
```