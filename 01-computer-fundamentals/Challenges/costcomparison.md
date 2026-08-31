# Lesson 10 — Cloud Computing Introduction

## Challenge 2 — Cost Comparison: AWS EC2 vs. Physical Server

### Objective

Compare the cost of running a small web server using **Amazon EC2** versus purchasing and operating a physical server.

The goal is to understand the idea of a **break-even point**: the point where the total cost of the two options becomes equal.

---

## 1. AWS EC2

Amazon EC2 provides virtual servers in the AWS Cloud and uses usage-based pricing.

For example, AWS currently lists a **t3.micro** at **$0.0104/hour** for Linux/Unix in US East (Northern Virginia).

Assuming the server runs continuously:

**Monthly EC2 compute cost:**

`$0.0104 × 730 hours ≈ $7.59/month`

**Yearly compute cost:**

`$7.59 × 12 ≈ $91.08/year`

> This is only the EC2 compute cost. Storage, data transfer, and other AWS services can add additional costs.

---

## 2. Physical Server

A physical server requires an **upfront purchase**.

For a simplified example, assume:

* Physical server purchase: **$600**
* Electricity/maintenance are ignored for this basic comparison.
* The server is used continuously.

The important difference is:

**Physical server = large upfront cost**

**EC2 = ongoing usage-based cost**

---

## 3. Break-Even Point

We can calculate the simplified break-even point:

`Break-even months = Physical server cost ÷ Monthly EC2 cost`

Using the example:

`$600 ÷ $7.59 ≈ 79 months`

That's approximately:

**6.6 years**

So under these simplified assumptions, the physical server's purchase price would equal about **6.6 years of EC2 compute charges**.

---

## 4. Important Real-World Considerations

The calculation above is simplified.

A real comparison should also consider:

### Physical server costs

* Electricity
* Cooling
* Internet connection
* Hardware maintenance
* Hardware failures
* Replacement parts
* Physical space
* Upgrades
* Administration

### Cloud costs

* EC2 compute
* EBS storage
* Data transfer
* Additional AWS services
* Backups
* Monitoring

AWS also provides different purchasing options, such as On-Demand, Savings Plans, and Spot Instances, which can significantly change the cost.

---

## 5. Main Lesson

The cheapest option isn't automatically the best option.

Cloud computing can be valuable because you can obtain infrastructure **without buying and maintaining the physical hardware yourself**.

A physical server can become economically attractive over a long period if the workload is stable and the hardware is heavily utilized.

The correct decision depends on:

**Cost + workload + scalability + maintenance + reliability + flexibility**

---

### Key Concept

```text
Physical Server
      ↓
Large upfront cost
      ↓
Lower ongoing infrastructure cost
      ↓
Can become cheaper over a long period


AWS EC2
      ↓
Low/no hardware purchase
      ↓
Pay for usage
      ↓
Easy to scale
      ↓
Ongoing operating cost
```

### Conclusion

The break-even point depends entirely on the assumptions used. In this example, a **$600 physical server** compared with a continuously running **t3.micro at about $7.59/month** gives a simplified break-even point of approximately **79 months (6.6 years)**.
