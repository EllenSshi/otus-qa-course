SELECT d.name, p.model from oc_product_description as d inner join oc_product as p on d.product_id=p.product_id where d.name=%s and p.model=%s;