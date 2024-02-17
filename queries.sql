# Задание 1
select c.login, count(1) as "ordersCount"
from "Couriers" as c
inner join "Orders" as o on c.id = o."courierId"
where o."inDelivery" = true
group by c.login;


# Задание 2
select o.track,
	case when finished = true then 2 
		when cancelled = true then -1
		when "inDelivery" = true then 1
	else 0 end as status
from "Orders" as o;