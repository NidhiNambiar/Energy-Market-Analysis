-- Assess the liquidity of a stock by looking at the average volume traded every month. Higher volumes generally mean better liquidity, making it easier to execute trades without affecting the price too much.

--chevronstock
SELECT
    EXTRACT(YEAR FROM Date) AS Year,
    EXTRACT(MONTH FROM Date) AS Month,
    AVG(Volume) AS Average_Volume
FROM
    `learned-vault-378620.stocks_767.chevronstock`
GROUP BY
    Year, Month
ORDER BY
    Year, Month;