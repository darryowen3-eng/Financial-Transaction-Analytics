SELECT
	"Product_Name",
	COUNT("Product_Name") AS Total_products,
	SUM("Quantity"*"Price") AS Revenue
FROM financial_transactions ft
GROUP BY "Product_Name"
ORDER BY Revenue DESC;


CREATE MATERIALIZED VIEW top3_products AS (
WITH ranked_paymethod AS (
	SELECT
		"Payment_Method",
		"Product_Name",
		"Quantity"*"Price" AS Revenue,
		dense_rank() OVER(
			PARTITION BY "Payment_Method"
			ORDER BY "Quantity"*"Price" DESC
		) AS ranked_payment_method
	FROM financial_transactions ft 
)
SELECT *
FROM ranked_paymethod
WHERE ranked_payment_method <= 3
);


WITH risk_tracking AS (
	SELECT
		"Payment_Method",
		"Transaction_Status",
		COUNT("Transaction_Status") AS total_failed_transaction
	FROM financial_transactions ft
	GROUP BY "Payment_Method", "Transaction_Status"
	HAVING "Transaction_Status" = 'Failed'
	ORDER BY total_failed_transaction desc
),
status_rankin AS (
	SELECT *,
		CASE
			WHEN total_failed_transaction > 10000 THEN 'High Risk'
			ELSE 'Moderate Risk'
		END AS risk_status
	FROM risk_tracking
)
SELECT *
FROM status_rankin;
	

WITH grouped_year AS(
	SELECT
		to_char("Transaction_Date"::Date, 'YYYY') AS year,
		SUM("Quantity"*"Price") AS total_revenue
	FROM financial_transactions ft
	GROUP BY year
	HAVING to_char("Transaction_Date"::Date, 'YYYY') != '2005'
),
lagging_rev AS (
	SELECT *,
		lag(total_revenue) OVER(
			ORDER BY YEAR
		) AS lagged_revenue,
		total_revenue - lag(total_revenue) OVER(
			ORDER BY YEAR
		) AS growth_per_year
	FROM grouped_year 
)
SELECT *
FROM lagging_rev;





