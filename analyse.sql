-- 1. What was the total revenue to the nearest dollar for customers who have paid by credit card?
SELECT ROUND(SUM(revenue)) AS total_revenue
FROM user_behaviour
WHERE cc_payments > 0;

-- 2. What percentage of customers who have purchased female items have paid by credit card?
WITH customers_with_female_items AS (
    SELECT customer_id, cc_payments
    FROM user_behaviour 
    WHERE female_items > 0
)
SELECT 
    ROUND(
        100.0 * COUNT(CASE WHEN cc_payments > 0 THEN 1 END) / COUNT(customer_id),
        2
    ) AS percentage_female_item_cc_payment
FROM customers_with_female_items;

-- 3. What was the average revenue for customers who used either iOS, Android or Desktop?
SELECT CAST(AVG(revenue) AS DECIMAL(10,2)) AS average_revenue
FROM user_behaviour
WHERE ios_orders > 0 OR android_orders > 0 OR desktop_orders > 0;


-- 4. We want to run an email campaign promoting a new men's luxury brand. Can you provide a list of customers we should send to?
SELECT customer_id
FROM user_behaviour
WHERE 
    is_newsletter_subscriber = 'Y'
    AND (mapp_items > 0 OR mftw_items > 0 OR macc_items > 0 OR mspt_items > 0) 
ORDER BY revenue DESC;