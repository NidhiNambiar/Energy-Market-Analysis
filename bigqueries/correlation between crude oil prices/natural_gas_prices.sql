-- Is there a correlation between crude oil prices and the natural gas prices
SELECT
    corr(t1.value, t2.value)
  FROM
    `learned-vault-378620.crudedataset.crudeprice` AS t1
    INNER JOIN `learned-vault-378620.crudedataset.naturalgasprice` AS t2 ON t1.date = t2.date
