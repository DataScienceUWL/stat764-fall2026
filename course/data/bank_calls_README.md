# Bank telemarketing calls — Mini-project 1 data

A Portuguese bank phoned its clients to sell a **term deposit**. Each row is one call: who the
client is, what the bank knew about past contact with them, the economic conditions at the time,
and whether the client said yes.

## The two files

| file | rows | what is in it |
|---|---|---|
| `bank_calls.csv` | 37,069 calls | every column, including the outcome `y` |
| `bank_hidden_calls.csv` | 4,119 calls | only what the bank knows **before it dials** — no `y`, and no `duration` |

The hidden calls are a random 10% of the original 41,188, set aside before you ever saw the data.
You hand in predictions for them once; I score them once.

Load them the usual way:

```python
from stat764 import load
calls = load("bank_calls.csv")
hidden = load("bank_hidden_calls.csv")
```

**`call_id`** is each call's row number in the original file, which is in **date order, from May
2008 to November 2010**. There is no date column; `call_id` is the only record of when a call
happened. It is an identifier, not a measurement.

## The columns

**The client**

| column | what it is |
|---|---|
| `age` | age in years |
| `job` | type of job (admin., blue-collar, entrepreneur, housemaid, management, retired, self-employed, services, student, technician, unemployed, unknown) |
| `marital` | married, single, divorced (which includes widowed), unknown |
| `education` | basic.4y, basic.6y, basic.9y, high.school, illiterate, professional.course, university.degree, unknown |
| `default` | has credit in default? yes, no, unknown |
| `housing` | has a housing loan? yes, no, unknown |
| `loan` | has a personal loan? yes, no, unknown |

**The last contact in this campaign**

| column | what it is |
|---|---|
| `contact` | how the client was reached: cellular or telephone |
| `month` | month of the last contact (jan … dec) |
| `day_of_week` | weekday of the last contact (mon … fri) |
| `duration` | length of the last contact, in seconds |

**Contact history**

| column | what it is |
|---|---|
| `campaign` | number of contacts with this client during this campaign, including the last one |
| `pdays` | days since the client was last contacted in a previous campaign; **999 means never contacted before** |
| `previous` | number of contacts with this client before this campaign |
| `poutcome` | outcome of the previous campaign: failure, success, nonexistent |

**The economy at the time of the call** (national indicators published by the Banco de Portugal)

| column | what it is |
|---|---|
| `emp.var.rate` | employment variation rate (quarterly) |
| `cons.price.idx` | consumer price index (monthly) |
| `cons.conf.idx` | consumer confidence index (monthly) |
| `euribor3m` | 3-month Euribor interest rate (daily) |
| `nr.employed` | number employed (quarterly, in thousands) |

**The outcome**

| column | what it is |
|---|---|
| `y` | did the client subscribe to a term deposit? yes / no |

Missing values in the categorical columns are coded as the word **`unknown`**, not left blank.
Whether that is a category, a missing value, or something to think harder about is your call —
and part of your data-quality section.

## Source and license

UCI Machine Learning Repository, *Bank Marketing* dataset, `bank-additional-full.csv`
(doi:10.24432/C5K306), licensed CC BY 4.0. Described in: S. Moro, P. Cortez and P. Rita, "A
data-driven approach to predict the success of bank telemarketing," *Decision Support Systems*
62 (2014), 22–31, doi:10.1016/j.dss.2014.03.001. Changes made for this course: the `call_id`
column was added, the file was converted to comma-separated, and 10% of the calls were moved,
without their outcome and call duration, into `bank_hidden_calls.csv`.
