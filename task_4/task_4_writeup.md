# Task 4: Data Analysis and Visualization with Pandas and Matplotlib: Writeup

## Setup

All questions use these imports. Figures are saved in `task_4/figures/`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# All figures are saved relative to the repository root, inside task_4/figures/
FIG_DIR = Path("task_4") / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
```

---

## Question 1: Fest Attendance Check

### Aim

Build a DataFrame of the fest events, add an attendance rate, and compare the event with the most registrations against the event with the best attendance rate.

### Code

```python
events = {'event': ['City Scaping', 'salutes and ladders', 'Open Mic', '', 'Valorant tournament'],
          'registered': [180, 95, 140, 60, 210],
          'attended': [150, 70, 135, 52, 160],
          'fee': [200, 150, 0, 50, 100]}
df = pd.DataFrame(events)
print("Shape (before new column):", df.shape)
print("\nDtypes:\n", df.dtypes)

df['attendance_rate'] = (df['attended'] / df['registered'] * 100).round(1)
print("\n", df)

most_reg = df.loc[df['registered'].idxmax()]
best_rate = df.loc[df['attendance_rate'].idxmax()]
print("\nMost registrations :", most_reg['event'], "-", most_reg['registered'], "registered, rate", most_reg['attendance_rate'])
print("Best attendance rate:", best_rate['event'], "-", best_rate['attendance_rate'], "%")
```

### Output

```
Shape (before new column): (5, 4)

Dtypes:
 event           str
registered    int64
attended      int64
fee           int64
dtype: object

                  event  registered  attended  fee  attendance_rate
0         City Scaping         180       150  200             83.3
1  salutes and ladders          95        70  150             73.7
2             Open Mic         140       135    0             96.4
3                               60        52   50             86.7
4  Valorant tournament         210       160  100             76.2

Most registrations : Valorant tournament - 210 registered, rate 76.2
Best attendance rate: Open Mic - 96.4 %
```

### Explanation

`pd.DataFrame(dict)` turns each key into a column. `shape` is `(5, 4)` before the new column, and `dtypes` shows `event` as `object` (text) and the other three as `int64`. The rate is a vectorised calculation, `attended / registered * 100`, rounded with `.round(1)`. `idxmax()` returns the row label of the largest value, and `df.loc[...]` fetches that row.

Data note: the task's Expected line calls the 210-registration event "Gaming Arena", but the data as given names it `Valorant tournament`, so the output uses that name (same numbers: 210 registrations, rate 76.2). The data also contains one event with an empty name (`''`, 60 registered); it was left unchanged because the question did not ask for cleaning.

**Interpret:** They are not the same event. Valorant tournament has the most registrations (210) but only a 76.2% attendance rate, while Open Mic has fewer registrations (140) but the best rate (96.4%). Registrations measure interest, not turnout, so judging an event by registrations alone overstates the events where many people sign up and then do not show up.

---

## Question 2: Fitness Tracker Week

### Aim

Turn a NumPy array of one week of fitness data into a labelled DataFrame, fix the integer columns, and find the busiest and the shortest-sleep days.

### Code

```python
data = np.array([[8200, 7.5, 40], [10400, 6.5, 55], [6100, 8.0, 20], [12000, 6.0, 70],
                 [9800, 7.0, 50], [3000, 9.0, 10], [7500, 8.5, 35]])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

fit = pd.DataFrame(data, index=days, columns=['steps', 'sleep_hours', 'active_minutes'])
fit = fit.astype({'steps': int, 'active_minutes': int})
print(fit)
print("\nDtypes:\n", fit.dtypes)

print("\n", fit.describe().round(2))
print("\nAverage steps :", round(fit['steps'].mean(), 2))
print("Average sleep :", fit['sleep_hours'].mean())
print("Most steps    :", fit['steps'].idxmax())
print("Least sleep   :", fit['sleep_hours'].idxmin())
```

### Output

```
     steps  sleep_hours  active_minutes
Mon   8200          7.5              40
Tue  10400          6.5              55
Wed   6100          8.0              20
Thu  12000          6.0              70
Fri   9800          7.0              50
Sat   3000          9.0              10
Sun   7500          8.5              35

Dtypes:
 steps               int64
sleep_hours       float64
active_minutes      int64
dtype: object

           steps  sleep_hours  active_minutes
count      7.00         7.00            7.00
mean    8142.86         7.50           40.00
std     2993.25         1.08           20.62
min     3000.00         6.00           10.00
25%     6800.00         6.75           27.50
50%     8200.00         7.50           40.00
75%    10100.00         8.25           52.50
max    12000.00         9.00           70.00

Average steps : 8142.86
Average sleep : 7.5
Most steps    : Thu
Least sleep   : Thu
```

### Explanation

A 2-D NumPy array has no labels, so `index=days` and `columns=[...]` give the rows and columns names. Mixed values in one array become floats, so `astype({'steps': int, 'active_minutes': int})` restores integer columns while leaving `sleep_hours` as float. `describe()` gives count, mean, std, quartiles, min and max for each column. The mean steps are 8142.86 and the mean sleep is 7.5 hours. `idxmax()` and `idxmin()` return the row labels, and both point to Thu (12000 steps, 6.0 hours of sleep).

**Interpret:** Seven rows only show that the busiest day was also the shortest sleep day. It could be a coincidence, so it cannot show that activity causes short sleep. I would want many more weeks of data, bedtime and wake-up times, caffeine or screen time, workload (exam or work days), and the time of day the steps were taken, since a late workout affects sleep differently from a morning walk.

---

## Question 3: Spotify Song List

### Aim

Explore a song table, list the top 3 songs by streams, and find songs that are both popular and frequently skipped.

### Code

```python
songs = {'song': ['Neon Drive', 'Monsoon Loop', 'Gravity', 'Night Bus', 'Cherry Static', 'Dust Roads', 'Run It Back', 'Paper Moon'],
         'genre': ['Pop', 'LoFi', 'Rock', 'LoFi', 'Pop', 'Folk', 'HipHop', 'Folk'],
         'streams_k': [520, 310, 450, 280, 610, 150, 390, 205],
         'skip_pct': [18, 9, 32, 12, 41, 7, 27, 10],
         'duration_sec': [201, 245, 289, 198, 176, 310, 187, 262]}
sp = pd.DataFrame(songs)

print("Shape :", sp.shape)
print("Dtypes:\n", sp.dtypes)
print("\nDistinct genres:", sp['genre'].nunique())

print("\nTop 3 by streams:\n", sp.nlargest(3, 'streams_k')[['song', 'streams_k']])

risky = sp[(sp['streams_k'] > 400) & (sp['skip_pct'] > 25)]
print("\nPopular (>400k) and skipped (>25%):\n", risky[['song', 'streams_k', 'skip_pct']])
```

### Output

```
Shape : (8, 5)
Dtypes:
 song              str
genre             str
streams_k       int64
skip_pct        int64
duration_sec    int64
dtype: object

Distinct genres: 5

Top 3 by streams:
             song  streams_k
4  Cherry Static        610
0     Neon Drive        520
2        Gravity        450

Popular (>400k) and skipped (>25%):
             song  streams_k  skip_pct
2        Gravity        450        32
4  Cherry Static        610        41
```

### Explanation

`nunique()` counts the distinct values in a column (5 genres: Pop, LoFi, Rock, Folk, HipHop). `nlargest(3, 'streams_k')` returns the three rows with the highest streams: Cherry Static (610), Neon Drive (520) and Gravity (450). For the combined filter, each condition goes in parentheses and the two are joined with `&`, because Python's `and` does not work element-wise on Series. Only Gravity (32% skipped) and Cherry Static (41% skipped) pass both tests.

**Interpret:** Two of the three most-streamed songs are skipped by a large share of listeners. If the platform recommends songs using stream counts only, it keeps pushing tracks that many listeners abandon quickly, which can hurt satisfaction and retention. Skip rate (or completion rate) should be used alongside streams.

---

## Question 4: Mess Rush Hour

### Aim

Index canteen data by hour, then compare label-based (`loc`) and position-based (`iloc`) selection and find the busy hours with a Boolean mask.

### Code

```python
canteen = {'hour': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
           'sold': [40, 55, 35, 90, 210, 180, 60, 30, 70, 95],
           'prepared': [50, 60, 50, 100, 220, 230, 80, 60, 90, 110]}
cant = pd.DataFrame(canteen).set_index('hour')

by_loc = cant.loc[11:13, 'sold']
by_iloc = cant.iloc[3:5]
busy = cant[cant['sold'] >= 90]

print("loc[11:13] ->", len(by_loc), "rows\n", by_loc)
print("\niloc[3:5] ->", len(by_iloc), "rows\n", by_iloc)
print("\nBusy hours (sold >= 90):", busy.index.tolist(), "->", len(busy), "hours")
```

### Output

```
loc[11:13] -> 3 rows
 hour
11     90
12    210
13    180
Name: sold, dtype: int64

iloc[3:5] -> 2 rows
       sold  prepared
hour                
11      90       100
12     210       220

Busy hours (sold >= 90): [11, 12, 13, 17] -> 4 hours
```

### Explanation

`set_index('hour')` makes the hour the row label. `loc` selects by label and its slice includes both ends, so `loc[11:13]` returns hours 11, 12 and 13 (3 rows). `iloc` selects by integer position and its slice excludes the end, like normal Python slicing, so `iloc[3:5]` returns positions 3 and 4 (the rows for hours 11 and 12), which is 2 rows. The Boolean mask `sold >= 90` finds the busy hours 11, 12, 13 and 17.

**Interpret:** `loc[11:13]` and `iloc[3:5]` return different numbers of rows because `loc` slices are inclusive of the end label, while `iloc` slices stop before the end position.

---

## Question 5: Is the Busiest Hour the Most Wasteful?

### Aim

Using the canteen data from Question 4, measure waste in items and in percent, and decide which hour to cut preparation in.

### Code

```python
# Continues from Question 4 (the `cant` DataFrame indexed by hour)
cant['waste'] = cant['prepared'] - cant['sold']
cant['waste_pct'] = (cant['waste'] / cant['prepared'] * 100).round(1)
print(cant)

print(f"\n(a) Most items sold      : {cant['sold'].idxmax()}:00")
print(f"(b) Highest waste (items): {cant['waste'].idxmax()}:00 with {cant['waste'].max()} items")
print(f"(c) Highest waste (%)    : {cant['waste_pct'].idxmax()}:00 with {cant['waste_pct'].max()}%")
```

### Output

```
      sold  prepared  waste  waste_pct
hour                                  
8       40        50     10       20.0
9       55        60      5        8.3
10      35        50     15       30.0
11      90       100     10       10.0
12     210       220     10        4.5
13     180       230     50       21.7
14      60        80     20       25.0
15      30        60     30       50.0
16      70        90     20       22.2
17      95       110     15       13.6

(a) Most items sold      : 12:00
(b) Highest waste (items): 13:00 with 50 items
(c) Highest waste (%)    : 15:00 with 50.0%
```

### Explanation

`waste = prepared - sold` and `waste_pct = waste / prepared * 100` are vectorised column operations. The three answers are different hours: the best-selling hour is 12:00 (210 sold), the largest absolute waste is 13:00 (50 items), and the largest percentage waste is 15:00 (50.0%).

**Decision:** I would cut preparation at 13:00. It wastes the most items (50), so it offers the largest saving, and it still sells 180 items, so preparing about 190 instead of 230 keeps a small buffer. The 15:00 hour has the worst percentage, but it prepares only 60 items, so cutting there saves at most 30 items. The saving from 13:00 is bigger in absolute terms.

---

## Question 6: Online Store Catalog Search

### Aim

Answer four manager questions about a product catalog, each with a single filter.

### Code

```python
catalog = {'product': ['USB-C Hub Pro', 'Notebook A5', 'Gel Pen Pack', 'Laptop Stand Pro',
                       'Desk Lamp', 'Mouse Pad XL', 'Webcam Pro', 'Sticky Notes'],
           'category': ['Electronics', 'Stationery', 'Stationery', 'Electronics',
                        'Home', 'Accessories', 'Electronics', 'Stationery'],
           'price': [1299, 120, 90, 1599, 899, 349, 2499, 60],
           'units_sold': [85, 400, 520, 60, 110, 230, 25, 610]}
cat = pd.DataFrame(catalog)

a = cat[cat['product'].str.contains('Pro')]
b = cat[cat['category'].isin(['Stationery', 'Home'])]
c = cat[cat['price'].between(300, 1500)]
d = cat[cat['product'].str.contains('Pro') & (cat['units_sold'] < 70)]

for label, res in [("(a) name contains 'Pro'", a), ("(b) Stationery or Home", b),
                   ("(c) price 300-1500", c), ("(d) Pro and < 70 units", d)]:
    print(f"{label}: {len(res)} products ->", res['product'].tolist())
```

### Output

```
(a) name contains 'Pro': 3 products -> ['USB-C Hub Pro', 'Laptop Stand Pro', 'Webcam Pro']
(b) Stationery or Home: 4 products -> ['Notebook A5', 'Gel Pen Pack', 'Desk Lamp', 'Sticky Notes']
(c) price 300-1500: 3 products -> ['USB-C Hub Pro', 'Desk Lamp', 'Mouse Pad XL']
(d) Pro and < 70 units: 2 products -> ['Laptop Stand Pro', 'Webcam Pro']
```

### Explanation

- `str.contains('Pro')` filters by text inside the product name (3 products).
- `isin([...])` keeps rows whose value is in a list (4 products).
- `between(300, 1500)` is inclusive on both ends (3 products: 1299, 349 and 899).
- (d) combines the text filter with a numeric condition using `&` (2 products: Laptop Stand Pro with 60 units and Webcam Pro with 25).

**Interpret:** Two of the three Pro products sold fewer than 70 units, and they are also the two most expensive items (1599 and 2499). Premium products sell poorly in this store, which mostly sells cheap items such as stationery. The store should be careful about stocking many high-priced items.

---

## Question 7: The Faulty Manipal Weather Station

### Aim

Count and handle missing readings, and explain why the median is a safer fill value than the mean when a sensor fault produces an extreme value.

### Code

```python
weather = pd.DataFrame({'day': range(1, 11),
                        'temp_c': [28.1, 29.0, np.nan, 30.2, 29.5, 55.0, np.nan, 27.8, 28.6, 29.3],
                        'humidity': [64, 61, 63, np.nan, 60, 58, np.nan, 66, 65, 62]})

print("Missing per column:\n", weather.isna().sum())
print("\nRows with at least one missing value:", weather.isna().any(axis=1).sum())

# Statistics of the original readings (NaN ignored)
print("\nTemp mean  :", round(weather['temp_c'].mean(), 2))
print("Temp median:", weather['temp_c'].median())

# Drop rows where BOTH readings are missing, then fill the rest with the column median
clean = weather.dropna(subset=['temp_c', 'humidity'], how='all')
print("\nRows remaining after dropping:", len(clean))
clean = clean.fillna({'temp_c': clean['temp_c'].median(),
                      'humidity': clean['humidity'].median()})
print(clean)
```

### Output

```
Missing per column:
 day         0
temp_c      2
humidity    2
dtype: int64

Rows with at least one missing value: 3

Temp mean  : 32.19
Temp median: 29.15

Rows remaining after dropping: 9
   day  temp_c  humidity
0    1   28.10      64.0
1    2   29.00      61.0
2    3   29.15      63.0
3    4   30.20      62.5
4    5   29.50      60.0
5    6   55.00      58.0
7    8   27.80      66.0
8    9   28.60      65.0
9   10   29.30      62.0
```

### Explanation

`isna().sum()` counts missing values per column (2 each), and `isna().any(axis=1).sum()` counts the rows with at least one gap (3: days 3, 4 and 7). `dropna(subset=[...], how='all')` removes only rows where both readings are missing, which is day 7, leaving 9 rows. `fillna()` with a dictionary fills each column with its own median.

**Interpret:** The temperature mean is 32.19 but the median is 29.15. The faulty 55.0 °C reading of day 6 drags the mean far above every other reading, while the median ignores how extreme that value is. Filling gaps with the mean would put impossible-looking temperatures (about 32 °C) into days that were around 28-30 °C, so the median is the safer choice.

---

## Question 8: Duplicate Orders and Messy Product Names

### Aim

Clean duplicate and inconsistently written orders and measure how much the bad data inflated revenue.

### Code

```python
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 101, 104, 105, 106, 105],
    'customer': ['Asha', 'ravi', 'Meera', 'Asha', 'Kiran', 'ravi', 'Meera', 'Ravi'],
    'product': ['laptop bag', 'Laptop Bag ', 'desk lamp', 'laptop bag', 'DESK LAMP', 'notebook', 'Notebook', 'Notebook '],
    'amount': [1200, 1200, 900, 1200, 900, 150, 150, 150]})

print("Rows (raw)                      :", len(orders))
print("Rows after raw drop_duplicates():", len(orders.drop_duplicates()))
raw_revenue = orders['amount'].sum()

clean = orders.copy()
clean['customer'] = clean['customer'].str.strip().str.title()
clean['product'] = clean['product'].str.strip().str.title()
clean = clean.drop_duplicates()
clean_revenue = clean['amount'].sum()

print("Rows after cleaning + dedupe    :", len(clean))
print("Distinct products after cleaning:", clean['product'].nunique())
print("\nRevenue raw    :", raw_revenue)
print("Revenue cleaned:", clean_revenue)
print("Overstatement  :", round((raw_revenue - clean_revenue) / clean_revenue * 100, 1), "%")
print("\n", clean)
```

### Output

```
Rows (raw)                      : 8
Rows after raw drop_duplicates(): 7
Rows after cleaning + dedupe    : 6
Distinct products after cleaning: 3

Revenue raw    : 5850
Revenue cleaned: 4500
Overstatement  : 30.0 %

    order_id customer     product  amount
0       101     Asha  Laptop Bag    1200
1       102     Ravi  Laptop Bag    1200
2       103    Meera   Desk Lamp     900
4       104    Kiran   Desk Lamp     900
5       105     Ravi    Notebook     150
6       106    Meera    Notebook     150
```

### Explanation

`drop_duplicates()` only removes rows that are identical in every column. On the raw data only the two `101` rows match exactly (8 to 7 rows). Order 105 was missed because `'ravi'` and `'Ravi'`, and `'Notebook'` and `'Notebook '` (trailing space), look different to Python. After `str.strip()` and `str.title()` make the text consistent, the second 105 row becomes an exact duplicate and is removed (6 rows). Cleaning also merges the product spellings into 3 distinct products: Laptop Bag, Desk Lamp and Notebook.

**Interpret:** Raw revenue is 5850 and the cleaned revenue is 4500, so bad data inflated revenue by 30.0%. The first attempt missed a duplicate because it compared strings exactly, and differences in capitalisation and spaces made the same order look like a different one.

---

## Question 9: Player Efficiency

### Aim

Create derived columns with vectorised arithmetic, `apply` and `map`, and check whether the top scorer is also the most efficient.

### Code

```python
players = pd.DataFrame({'player': ['A', 'B', 'C', 'D', 'E', 'F'],
                        'score': [4200, 1800, 7600, 3100, 5900, 900],
                        'minutes': [30, 45, 60, 20, 40, 15]})

players['score_per_min'] = (players['score'] / players['minutes']).round(1)

def tier(score):
    if score >= 6000:
        return 'Elite'
    elif score >= 3000:
        return 'Skilled'
    return 'Rookie'

players['tier'] = players['score'].apply(tier)
players['bonus'] = players['tier'].map({'Elite': 500, 'Skilled': 200, 'Rookie': 50})

print(players)
print("\nTotal bonus:", players['bonus'].sum())
print("Top scorer       :", players.loc[players['score'].idxmax(), 'player'])
print("Most efficient   :", players.loc[players['score_per_min'].idxmax(), 'player'])
```

### Output

```
  player  score  minutes  score_per_min     tier  bonus
0      A   4200       30          140.0  Skilled    200
1      B   1800       45           40.0   Rookie     50
2      C   7600       60          126.7    Elite    500
3      D   3100       20          155.0  Skilled    200
4      E   5900       40          147.5  Skilled    200
5      F    900       15           60.0   Rookie     50

Total bonus: 1200
Top scorer       : C
Most efficient   : D
```

### Explanation

`score / minutes` is a vectorised operation applied to the whole column at once. `apply(tier)` runs a small function on each score, and `map({...})` swaps each tier label for its bonus value through a dictionary. The tiers are C Elite; A, D and E Skilled; B and F Rookie. The bonus total is 500 + 3 x 200 + 2 x 50 = 1200.

**Interpret:** The top scorer is C (7600 points) but C is not the most efficient. Player D has the best `score_per_min` (155.0), against 126.7 for C, because D scored 3100 points in only 20 minutes.

---

## Question 10: Do Mid-Sem Averages Hide Inconsistency?

### Aim

Compare subjects by mean and by spread in one `agg` call, and spot which subject has an inconsistent result hiding behind its average.

### Code

```python
marks = pd.DataFrame({
    'subject': ['Maths']*4 + ['Physics']*4 + ['Pps']*4,
    'marks': [72, 74, 70, 73, 60, 95, 50, 85, 80, 78, 82, 84]})

stats = marks.groupby('subject')['marks'].agg(['mean', 'std', 'min', 'max']).round(2)
print(stats)
print("\nRanked by mean (high to low):\n", stats['mean'].sort_values(ascending=False))
print("\nRanked by std (high to low):\n", stats['std'].sort_values(ascending=False))
```

### Output

```
          mean    std  min  max
subject                        
Maths    72.25   1.71   70   74
Physics  72.50  21.02   50   95
Pps      81.00   2.58   78   84

Ranked by mean (high to low):
 subject
Pps        81.00
Physics    72.50
Maths      72.25
Name: mean, dtype: float64

Ranked by std (high to low):
 subject
Physics    21.02
Pps         2.58
Maths       1.71
Name: std, dtype: float64
```

### Explanation

`groupby('subject')['marks'].agg([...])` computes several statistics per group in a single call. The pandas default for `std` is the sample standard deviation (`ddof=1`). The means are Maths 72.25, Physics 72.5 and Pps 81.0. The standard deviations are 1.71, 21.02 and 2.58.

Data note: the Expected line calls the third subject "Programming", but the data labels it `Pps` (the same 81.0 mean and 2.58 std), so the output keeps the label from the data.

**Interpret:** Maths and Physics have almost the same average (72.25 and 72.5), but Physics has a huge spread (std 21.02, marks from 50 to 95) compared with Maths (1.71). A teacher should investigate Physics: the average hides a split between students who understand the subject and students who are struggling, possibly caused by a difficult paper, uneven teaching or different prior knowledge.

---

## Question 11: Highest Revenue, Highest Profit?

### Aim

Compare products by total revenue, total profit and profit margin to decide which product deserves the promotion budget.

### Code

```python
sales = pd.DataFrame({
    'product': ['Phone Case', 'Phone Case', 'Earbuds', 'Earbuds', 'Smart Watch', 'Smart Watch',
                'Power Bank', 'Power Bank', 'Screen Guard', 'Screen Guard'],
    'month': ['Aug', 'Sep'] * 5,
    'units': [180, 120, 100, 50, 50, 40, 90, 110, 300, 200],
    'price': [299, 299, 1499, 1499, 2999, 2999, 999, 999, 99, 99],
    'cost': [120, 120, 1300, 1300, 2700, 2700, 650, 650, 40, 40]})

sales['revenue'] = sales['units'] * sales['price']
sales['profit'] = sales['units'] * (sales['price'] - sales['cost'])

summary = sales.groupby('product')[['revenue', 'profit']].sum()
summary['margin_pct'] = (summary['profit'] / summary['revenue'] * 100).round(1)

print(summary.sort_values('revenue', ascending=False))
print("\nHighest revenue:", summary['revenue'].idxmax(), summary['revenue'].max())
print("Highest profit :", summary['profit'].idxmax(), summary['profit'].max())
print("Best margin    :", summary['margin_pct'].idxmax(), summary['margin_pct'].max())
```

### Output

```
              revenue  profit  margin_pct
product                                  
Smart Watch    269910   26910        10.0
Earbuds        224850   29850        13.3
Power Bank     199800   69800        34.9
Phone Case      89700   53700        59.9
Screen Guard    49500   29500        59.6

Highest revenue: Smart Watch 269910
Highest profit : Power Bank 69800
Best margin    : Phone Case 59.9
```

### Explanation

Revenue is `units x price` and profit is `units x (price - cost)` for each row. `groupby('product')` then `sum()` adds the months together, and the margin is calculated afterwards from the totals. Smart Watch has the highest revenue (269,910) but a margin of only 10.0%. Power Bank has the highest profit (69,800).

**Decision:** Promote Power Bank. It earns the most profit with a healthy 34.9% margin. Smart Watch looks successful only because of its price: each sale brings a lot of revenue but only 299 profit on a 2999 price. Phone Case (59.9% margin) and Screen Guard (59.6%) have the best margins, so they are also good promotion candidates if the aim is margin rather than total profit.

---

## Question 12: The Misleading Conversion Rate

### Aim

Show why averaging row-level rates is wrong when the visitor counts differ greatly, and correct it by summing first and dividing afterwards.

### Code

```python
funnel = pd.DataFrame({'channel': ['A', 'A', 'B', 'B'],
                       'visitors': [10, 490, 100, 100],
                       'signups': [6, 49, 20, 20]})

# Teammate's flawed approach: average of row-level rates
funnel['rate'] = funnel['signups'] / funnel['visitors'] * 100
print("Flawed (mean of rates):\n", funnel.groupby('channel')['rate'].mean())

# Correct approach: aggregate first, compute the rate afterwards
totals = funnel.groupby('channel')[['visitors', 'signups']].sum()
totals['rate'] = totals['signups'] / totals['visitors'] * 100
print("\nCorrect (total signups / total visitors):\n", totals)
```

### Output

```
Flawed (mean of rates):
 channel
A    35.0
B    20.0
Name: rate, dtype: float64

Correct (total signups / total visitors):
          visitors  signups  rate
channel                         
A             500       55  11.0
B             200       40  20.0
```

### Explanation

The flawed code gives A = 35.0 and B = 20.0. Channel A has two rows: 6 signups from only 10 visitors (60%) and 49 from 490 visitors (10%). The plain mean treats these two rows as equally important, even though the 10-visitor row represents about 2% of the channel's traffic. The correct method sums the counts first: A has 55 signups from 500 visitors (11.0%) and B has 40 from 200 visitors (20.0%).

**Decision:** Jio should invest in channel B. Its true conversion rate (20.0%) is almost double that of A (11.0%). Channel A only looked better because a tiny sample produced an extreme rate.

---

## Question 13: The Catalog Gap

### Aim

Compare inner, left and outer joins on a track catalog and play counts, and build a report of every catalog track.

### Code

```python
tracks = pd.DataFrame({'track_id': [1, 2, 3, 4],
                       'title': ['Neon Drive', 'Gravity', 'Night Bus', 'Dust Roads'],
                       'artist': ['Aria', 'Vega', 'Aria', 'Mohan']})
plays = pd.DataFrame({'track_id': [1, 2, 3, 5], 'plays': [520, 450, 280, 90]})

for how in ['inner', 'left', 'outer']:
    print(f"{how:5s} join rows:", len(tracks.merge(plays, on='track_id', how=how)))

report = tracks.merge(plays, on='track_id', how='left')
report['plays'] = report['plays'].fillna(0).astype(int)
print("\nLeft join report (every catalog track):\n", report)
print("\nTotal plays per artist:\n", report.groupby('artist')['plays'].sum())

print("\nPlay records with no catalog entry:\n",
      tracks.merge(plays, on='track_id', how='outer', indicator=True).query("_merge == 'right_only'"))
```

### Output

```
inner join rows: 3
left  join rows: 4
outer join rows: 5

Left join report (every catalog track):
    track_id       title artist  plays
0         1  Neon Drive   Aria    520
1         2     Gravity   Vega    450
2         3   Night Bus   Aria    280
3         4  Dust Roads  Mohan      0

Total plays per artist:
 artist
Aria     800
Mohan      0
Vega     450
Name: plays, dtype: int64

Play records with no catalog entry:
    track_id title artist  plays      _merge
4         5   NaN    NaN   90.0  right_only
```

### Explanation

The inner join keeps only matching ids (3 rows), the left join keeps every row from `tracks` (4 rows), and the outer join keeps everything from both tables (5 rows). A report that must list every catalog track needs the left join, with the catalog table on the left. Tracks without play records get `NaN`, which is filled with 0 (Dust Roads). Total plays are Aria 800, Vega 450 and Mohan 0.

**Interpret:** `track_id` 5 has 90 plays but is not in the catalog, so the play log refers to a track the catalog does not know about (a missing catalog entry or a wrong id). Both the inner join and the left join hide it, because neither keeps unmatched rows from the right table. Only the outer join (with `indicator=True` to label the rows) shows it.

---

## Question 14: Delhi's Traffic and Air Quality

### Aim

Combine two weekly logs, measure the traffic-pollution correlation and compare the weekly means against an alert threshold.

### Code

```python
week1 = pd.DataFrame({'vehicles_k': [30, 35, 40, 45], 'pm25': [52, 55, 60, 63]})
week2 = pd.DataFrame({'vehicles_k': [50, 55, 60, 65], 'pm25': [68, 72, 75, 80]})

both = pd.concat([week1, week2], ignore_index=True)
print("Combined shape (before week column):", both.shape)
both['week'] = ['Week 1'] * 4 + ['Week 2'] * 4

print("Correlation (vehicles vs PM2.5):", round(both['vehicles_k'].corr(both['pm25']), 3))
weekly_mean = both.groupby('week')['pm25'].mean()
print("\nMean PM2.5 per week:\n", weekly_mean)
print("\nWeeks above the alert level of 70:", weekly_mean[weekly_mean > 70].index.tolist())
```

### Output

```
Combined shape (before week column): (8, 2)
Correlation (vehicles vs PM2.5): 0.999

Mean PM2.5 per week:
 week
Week 1    57.50
Week 2    73.75
Name: pm25, dtype: float64

Weeks above the alert level of 70: ['Week 2']
```

### Explanation

`pd.concat([...], ignore_index=True)` stacks the two tables and renumbers the index from 0 to 7. The `week` label is added afterwards. `Series.corr()` returns the Pearson correlation, about 0.999, a very strong positive relationship. The weekly means are 57.5 and 73.75.

**Interpret:** Week 2 triggers the alert, since its mean of 73.75 is above 70 (week 1 is 57.5). Traffic is not the only factor affecting PM2.5. Weather matters too: wind speed, rain, temperature inversions in winter, and humidity. Other sources such as construction dust, industrial emissions and crop burning also change PM2.5.

---

## Question 15: TechTatva Revenue Investigation

### Aim

Clean a messy registration sheet, remove repeated registrations, merge with fees and compute revenue by department, with and without removing duplicates.

### Code

```python
regs = pd.DataFrame({
    'reg_id': range(1, 12),
    'student': ['Anu', 'Bala', 'Chitra', 'Anu', 'Dev', 'Esha', 'Farhan', 'Gita', 'Bala', 'Hari', 'Ira'],
    'event': [' city landscaping ', 'city landscaping ', 'salutes and ladders', ' city landscaping ', 'Open Mic', 'open mic',
              'ROBO RACE', 'Quiz Night', 'hackathon', 'Quiz Night', 'Hackathon'],
    'dept': ['CSE', 'cse', 'ECE', 'CSE', 'MECH', 'CSE', 'ECE', None, 'CSE', 'ECE', 'ECE']})
fees = pd.DataFrame({'event': ['Hackathon', 'Robo Race', 'Open Mic', 'Quiz Night'],
                     'fee': [200, 150, 0, 50]})

# Clean the text and fill the missing department
regs['event'] = regs['event'].str.strip().str.title()
regs['dept'] = regs['dept'].str.upper().fillna('Unknown')

def revenue_by_dept(frame):
    merged = frame.merge(fees, on='event', how='left')   # left join keeps every registration
    return merged, merged.groupby('dept')['fee'].sum().sort_values(ascending=False)

# With duplicates removed: one registration per (student, event)
unique = regs.drop_duplicates(subset=['student', 'event'])
merged, dept_revenue = revenue_by_dept(unique)

print("Registrations after removing duplicates:", len(unique))
print("\nRegistrations per event:\n", unique['event'].value_counts())
print("\nEvents with no fee in the fee table:", sorted(merged.loc[merged['fee'].isna(), 'event'].unique()))
print("Total revenue:", merged['fee'].sum())
print("\nRevenue per department (duplicates removed):\n", dept_revenue)

_, dept_revenue_dup = revenue_by_dept(regs)
print("\nRevenue per department (duplicates kept):\n", dept_revenue_dup)
```

### Output

```
Registrations after removing duplicates: 10

Registrations per event:
 event
City Landscaping       2
Open Mic               2
Quiz Night             2
Hackathon              2
Salutes And Ladders    1
Robo Race              1
Name: count, dtype: int64

Events with no fee in the fee table: ['City Landscaping', 'Salutes And Ladders']
Total revenue: 650.0

Revenue per department (duplicates removed):
 dept
ECE        400.0
CSE        200.0
Unknown     50.0
MECH         0.0
Name: fee, dtype: float64

Revenue per department (duplicates kept):
 dept
ECE        400.0
CSE        200.0
Unknown     50.0
MECH         0.0
Name: fee, dtype: float64
```

### Explanation

Cleaning uses `str.strip()` and `str.title()` on the event names, `str.upper()` on departments (so `cse` and `CSE` match) and `fillna('Unknown')` for the missing department. `drop_duplicates(subset=['student', 'event'])` treats a repeated (student, event) pair as one registration: Anu registered twice for City Landscaping. A left merge keeps every registration even if its event has no fee.

Data note: the Expected values (9 registrations, Hackathon 3, Robo Race 2, total revenue 1000, ECE 550, CSE 400, and CSE 800 with duplicates) do not match the data as given. This data has 11 rows and only one repeated pair, so 10 registrations remain. Hackathon has 2 registrations and Robo Race has 1. Also, `City Landscaping` (3 raw rows, 2 after removing the duplicate) and `Salutes And Ladders` (1) are not in the `fees` table, so their fee is missing and counts as 0 in the revenue totals. The output above is what the given data produces: total revenue is 650, with ECE 400, CSE 200, Unknown 50 and MECH 0.

**Interpret:** In this data the duplicate is a City Landscaping registration, which has no fee listed, so keeping it does not change the department revenue (CSE is 200 either way). In general, though, duplicates inflate whichever department they belong to. If a duplicated registration had a fee, CSE would be overstated and could wrongly appear to lead. The committee should also add the missing fees for the City Landscaping and Salutes and Ladders events, because revenue is understated until they are known.

---

## Question 16: Manipal Weather Swings

### Aim

Plot daily high and low temperatures on one chart and use NumPy to find the day with the largest daily temperature range.

### Code

```python
days = np.arange(1, 11)
high = np.array([31, 32, 30, 29, 33, 35, 34, 28, 27, 30])
low = np.array([24, 25, 23, 24, 25, 26, 24, 22, 22, 23])

daily_range = high - low
swing_day = days[np.argmax(daily_range)]
print("Daily ranges (°C):", daily_range)
print("Largest range    :", daily_range.max(), "°C on day", swing_day)
print("Highest temp     :", high.max(), "°C on day", days[np.argmax(high)])

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(days, high, marker='o', linestyle='-', color='tab:red', label='Daily high')
ax.plot(days, low, marker='s', linestyle='--', color='tab:blue', label='Daily low')
ax.set_title('Manipal Daily High and Low Temperatures')
ax.set_xlabel('Day of the month (day number)')
ax.set_ylabel('Temperature (°C)')
ax.set_xticks(days)
ax.grid(True, alpha=0.3)
ax.legend()
fig.savefig(FIG_DIR / "q16_weather_swings.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
Daily ranges (°C): [ 7  7  7  5  8  9 10  6  5  7]
Largest range    : 10 °C on day 7
Highest temp     : 35 °C on day 6
```

![High and low temperatures over 10 days](figures/q16_weather_swings.png)

### Explanation

Subtracting the arrays (`high - low`) gives the daily range for all days at once, and `np.argmax` finds its position. The line chart uses different markers (circle and square) and line styles (solid and dashed) so the two series can be told apart, even in black and white.

**Interpret:** No. The highest temperature (35 °C) occurs on day 6, but the largest swing (10 °C) is on day 7, because day 7 had a high of 34 °C and a low of only 24 °C. The largest swing depends on the gap between high and low, not on how hot the day was.

---

## Question 17: Why Are Sales Falling?

### Aim

Add a total column with Pandas, plot the three series, and find which product category is driving the fall and which one is growing.

### Code

```python
store = pd.DataFrame({'month': ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
                      'phones': [120, 125, 118, 110, 95, 80],
                      'accessories': [60, 62, 65, 66, 70, 75]})
store['total'] = store['phones'] + store['accessories']
print(store)

first, last = store.iloc[0], store.iloc[-1]
print("\nTotal peak month:", store.loc[store['total'].idxmax(), 'month'], store['total'].max())
print("Change Apr -> Sep: total", last['total'] - first['total'],
      "| phones", last['phones'] - first['phones'],
      "| accessories", last['accessories'] - first['accessories'])

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(store['month'], store['phones'], marker='o', label='Phones')
ax.plot(store['month'], store['accessories'], marker='s', label='Accessories')
ax.plot(store['month'], store['total'], marker='^', linestyle='--', color='black', label='Total')
ax.set_title('Phones Are Falling While Accessories Keep Growing')
ax.set_xlabel('Month')
ax.set_ylabel('Sales (₹ lakh)')
ax.grid(True, alpha=0.3)
ax.legend()
fig.savefig(FIG_DIR / "q17_sales_trend.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
  month  phones  accessories  total
0   Apr     120           60    180
1   May     125           62    187
2   Jun     118           65    183
3   Jul     110           66    176
4   Aug      95           70    165
5   Sep      80           75    155

Total peak month: May 187
Change Apr -> Sep: total -25 | phones -40 | accessories 15
```

![Phones, accessories and total sales, April to September](figures/q17_sales_trend.png)

### Explanation

The `total` column is the row-wise sum of the two categories. Total sales peaked in May (187) and fell from 180 in April to 155 in September, a change of -25. Over the same period phones changed by -40 and accessories by +15. The total is drawn as a dashed black line so it stands out from the two categories.

**Interpret:** The owner's statement is only partly true. Total sales are falling, but not everything is declining. Phones drive the fall (from 120 to 80, and falling every month since May), while accessories are growing steadily (from 60 to 75) and are cushioning the drop. The store should find out why phones are declining (competition, pricing, stock) rather than treating the whole business as failing.

---

## Question 18: Who Is Buying the Tickets?

### Aim

Show daily ticket sales split by internal and external visitors, first as a stacked and then as a grouped bar chart, and compute the external share.

### Code

```python
day = ['Day 1', 'Day 2', 'Day 3']
internal = np.array([120, 150, 90])
external = np.array([30, 80, 160])

total = internal + external
share = (external / total * 100).round(1)
print("Daily totals        :", total)
print("External share (%)  :", {d: float(v) for d, v in zip(day, share)})

# Figure 1: stacked bars
fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.bar(day, internal, label='Internal', color='tab:blue')
ax1.bar(day, external, bottom=internal, label='External', color='tab:orange')
ax1.set_title('Tickets Sold per Day (Stacked)')
ax1.set_xlabel('Fest day')
ax1.set_ylabel('Tickets sold (count)')
ax1.legend()
fig1.savefig(FIG_DIR / "q18_tickets_stacked.png", dpi=150, bbox_inches="tight")
plt.show()

# Figure 2: grouped bars
x = np.arange(len(day))
width = 0.38
fig2, ax2 = plt.subplots(figsize=(7, 5))
ax2.bar(x - width / 2, internal, width, label='Internal', color='tab:blue')
ax2.bar(x + width / 2, external, width, label='External', color='tab:orange')
ax2.set_xticks(x)
ax2.set_xticklabels(day)
ax2.set_title('Tickets Sold per Day (Grouped)')
ax2.set_xlabel('Fest day')
ax2.set_ylabel('Tickets sold (count)')
ax2.legend()
fig2.savefig(FIG_DIR / "q18_tickets_grouped.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
Daily totals        : [150 230 250]
External share (%)  : {'Day 1': 20.0, 'Day 2': 34.8, 'Day 3': 64.0}
```

![Stacked bar chart of tickets per day](figures/q18_tickets_stacked.png)

![Grouped bar chart of tickets per day](figures/q18_tickets_grouped.png)

### Explanation

In the stacked chart each bar's height is the day's total, and the grouped chart places the two visitor types side by side. The totals are 150, 230 and 250, and the external shares are 20.0%, 34.8% and 64.0%.

**Design:** The stacked chart shows total footfall better, because the whole bar height is the daily total and the bars can be compared directly. The grouped chart compares internal against external visitors better, because both bars start from zero on the same baseline, whereas the top segment of a stacked bar starts at a different height on each day.

The fest was most dependent on outside visitors on Day 3, when external visitors made up 64.0% of tickets (160 out of 250).

---

## Question 19: Does Practice Really Drive Skill?

### Aim

Plot practice hours against skill rating, highlight the 20-hour player, and compare the correlation with and without that player.

### Code

```python
players = pd.DataFrame({'hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 20],
                        'rating': [50, 56, 48, 55, 52, 57, 49, 54, 51, 95]})

corr_all = players['hours'].corr(players['rating'])
typical = players[players['hours'] < 20]
corr_typical = typical['hours'].corr(typical['rating'])
print("Correlation, all 10 players        :", round(corr_all, 2))
print("Correlation, without the 20 h player:", round(corr_typical, 2))

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(typical['hours'], typical['rating'], color='tab:blue', s=60, label='Typical players')
top = players[players['hours'] == 20]
ax.scatter(top['hours'], top['rating'], color='tab:red', s=90, label='20-hour player')
ax.set_title('Practice Hours vs Skill Rating')
ax.set_xlabel('Practice (hours per week)')
ax.set_ylabel('Skill rating (points)')
ax.grid(True, alpha=0.3)
ax.legend()
fig.savefig(FIG_DIR / "q19_practice_vs_rating.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
Correlation, all 10 players        : 0.86
Correlation, without the 20 h player: 0.03
```

![Practice hours vs rating, 20-hour player highlighted](figures/q19_practice_vs_rating.png)

### Explanation

`Series.corr()` computes the Pearson correlation. With all ten players it is 0.86, which looks like strong support for the coach. After removing the 20-hour player, it falls to 0.03, which is essentially no relationship. The red point in the scatter plot sits far from the others and creates the correlation on its own.

**Interpret:** For typical players the data does not support the coach's claim: between 1 and 9 hours per week the ratings move between 48 and 57 with no pattern. One high-hours, high-rating player is enough to produce a strong correlation, so the 0.86 is driven by an outlier rather than a general trend. That player might be exceptionally talented, or something else could explain the rating.

---

## Question 20: Traffic Is Not the Whole Story

### Aim

Plot vehicles against PM2.5 with zone colours and population-sized markers, and find the stations that break the traffic-pollution pattern.

### Code

```python
stations = pd.DataFrame({
    'station': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'vehicles_k': [35, 40, 65, 60, 45, 50, 70, 30],
    'pm25': [58, 60, 80, 77, 110, 115, 83, 52],
    'zone': ['Residential', 'Residential', 'Commercial', 'Commercial',
             'Industrial', 'Industrial', 'Commercial', 'Residential'],
    'population_k': [40, 45, 30, 25, 15, 10, 35, 50]})

zone_colors = {'Residential': 'tab:green', 'Commercial': 'tab:blue', 'Industrial': 'tab:red'}
stations['color'] = stations['zone'].map(zone_colors)

fig, ax = plt.subplots(figsize=(8, 6))
for zone, grp in stations.groupby('zone'):
    ax.scatter(grp['vehicles_k'], grp['pm25'], s=grp['population_k'] * 8,
               c=grp['color'], alpha=0.7, edgecolors='black', label=zone)
for _, r in stations.iterrows():
    ax.annotate(r['station'], (r['vehicles_k'], r['pm25']), textcoords='offset points', xytext=(8, 6))
ax.set_title('Vehicles vs PM2.5 by Zone (marker size = population)')
ax.set_xlabel('Vehicles (thousands per day)')
ax.set_ylabel('PM2.5 (µg/m³)')
ax.grid(True, alpha=0.3)
ax.legend(title='Zone', labelspacing=1.5)
fig.savefig(FIG_DIR / "q20_traffic_pm25_zones.png", dpi=150, bbox_inches="tight")
plt.show()

print(stations[['station', 'zone', 'vehicles_k', 'pm25']].sort_values('pm25', ascending=False).head(3))
```

### Output

```
  station        zone  vehicles_k  pm25
5      S6  Industrial          50   115
4      S5  Industrial          45   110
6      S7  Commercial          70    83
```

![Vehicles vs PM2.5, coloured by zone](figures/q20_traffic_pm25_zones.png)

### Explanation

A dictionary `{zone: colour}` combined with `Series.map()` creates a colour for every station. Plotting one zone at a time with `groupby` gives each zone its own legend entry, and `s=population_k * 8` makes the marker area follow the population. The residential and commercial stations follow the expected pattern, with more vehicles meaning higher PM2.5.

**Interpret:** The two Industrial stations break the pattern. S5 and S6 record PM2.5 of 110 and 115 at only 45-50k vehicles, while the busiest station, S7 (70k vehicles, commercial), records only 83. The variable that explains them is the zone type, specifically industrial emissions, not traffic volume. They also have the smallest populations (15k and 10k), so the pollution is not caused by dense residential activity.

---

## Question 21: How Many Bins Is Too Many?

### Aim

Explain the problem with two histograms drawn on one axis, then draw them side by side on a shared 0-100 range with mean and median lines.

### Code

```python
scores = [12, 18, 22, 25, 28, 31, 33, 35, 38, 41, 44, 47, 52, 55, 58, 61, 67, 74, 88, 95]
mean, median = np.mean(scores), np.median(scores)
print("Mean:", round(mean, 1), "| Median:", median)

counts5, _ = np.histogram(scores, bins=5, range=(0, 100))
print("Counts with 5 bins over 0-100: ", counts5.tolist())
counts10, _ = np.histogram(scores, bins=10, range=(0, 100))
print("Counts with 10 bins over 0-100:", counts10.tolist())

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), sharex=True, sharey=True)
for ax, bins in zip(axes, [5, 10]):
    ax.hist(scores, bins=bins, range=(0, 100), color='tab:blue', edgecolor='white')
    ax.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean:.1f}')
    ax.axvline(median, color='green', linestyle='-.', label=f'Median = {median:.1f}')
    ax.set_title(f'{bins} bins (width {100 // bins})')
    ax.set_xlabel('Score (points)')
    ax.set_xlim(0, 100)
    ax.legend()
axes[0].set_ylabel('Number of players')
fig.suptitle('Scores of 20 Players on One Level')
fig.savefig(FIG_DIR / "q21_histograms.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
Mean: 46.2 | Median: 42.5
Counts with 5 bins over 0-100:  [2, 7, 6, 3, 2]
Counts with 10 bins over 0-100: [0, 2, 3, 4, 3, 3, 2, 1, 1, 1]
```

![Histograms with 5 and 10 bins, with mean and median](figures/q21_histograms.png)

### Explanation

**What is wrong with the teammate's code:** both `plt.hist` calls draw onto the same axes, so the 5-bin and the 10-bin histograms overlap and cannot be read. Neither call sets a range, so the bins cover only the data (12 to 95) rather than 0-100, and there are no titles, labels or reference lines. Separate subplots with `range=(0, 100)` and shared axes fix this.

With 5 bins over 0-100 the counts are [2, 7, 6, 3, 2]. The mean is 46.2 and the median is 42.5.

**Interpret:** The distribution is right-skewed: most players score between 20 and 60, with a long tail towards high scores (88 and 95). That is why the mean (46.2) is higher than the median (42.5). The 10-bin histogram (width 10) tells the story better, because it shows that the bulk of the scores sits between 20 and 60 and that the high scores are isolated. Five bins (width 20) are too coarse to show where within that range the players cluster, while many more bins on only 20 values would produce noisy bars with mostly 0, 1 or 2 players.

---

## Question 22: Which Level Is Unfair?

### Aim

Draw box plots of completion times and use the 1.5 x IQR rule in Pandas to list outliers.

### Code

```python
times = pd.DataFrame({
    'Level 1': [5, 6, 6, 7, 7, 8, 8, 9],
    'Level 2': [10, 11, 12, 12, 13, 14, 15, 40],
    'Level 3': [15, 16, 18, 18, 19, 20, 22, 24]})

q1, q3 = times.quantile(0.25), times.quantile(0.75)
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
summary = pd.DataFrame({'median': times.median(), 'IQR': iqr,
                        'lower_fence': lower, 'upper_fence': upper})
print(summary)

for level in times.columns:
    out = times[level][(times[level] < lower[level]) | (times[level] > upper[level])]
    print(f"Outliers in {level}:", out.tolist())

fig, ax = plt.subplots(figsize=(7, 5))
ax.boxplot([times[c] for c in times.columns])
ax.set_xticks([1, 2, 3], times.columns)
ax.set_title('Completion Time by Level')
ax.set_xlabel('Level')
ax.set_ylabel('Completion time (minutes)')
ax.grid(True, axis='y', alpha=0.3)
fig.savefig(FIG_DIR / "q22_level_boxplots.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
         median  IQR  lower_fence  upper_fence
Level 1     7.0  2.0          3.0         11.0
Level 2    12.5  2.5          8.0         18.0
Level 3    18.5  3.0         13.0         25.0
Outliers in Level 1: []
Outliers in Level 2: [40]
Outliers in Level 3: []
```

![Box plots of completion time for three levels](figures/q22_level_boxplots.png)

### Explanation

A box plot shows the median, the quartiles and any points beyond the whiskers. The medians are 7, 12.5 and 18.5. For Level 2, Q1 = 11.75 and Q3 = 14.25, so the IQR is 2.5 and the upper fence is 14.25 + 1.5 x 2.5 = 18.0. Any value above 18.0 is an outlier, so the 40 in Level 2 is flagged, and no other level has an outlier.

**Interpret:** Level 2 has the unusual completion time (40 minutes, while the next slowest player took 15). The designers should worry about one player, not the level: the other seven players took 10-15 minutes, so the level itself is not unfair. The 40-minute player may have been stuck, distracted, or hit a bug, which is worth checking, but redesigning the level is not justified by one result.

---

## Question 23: Goal Check Across Two Weeks

### Aim

Compare two weeks of daily steps against an 8000-step goal using side-by-side bar charts with a shared y-axis.

### Code

```python
week1 = [8200, 10400, 6100, 12000, 9800, 3000, 7500]
week2 = [9000, 11000, 8500, 7000, 12500, 5000, 9500]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
goal = 8000

for name, steps in [('Week 1', week1), ('Week 2', week2)]:
    s = np.array(steps)
    print(f"{name}: days meeting goal = {(s >= goal).sum()}, mean steps = {s.mean():.2f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
for ax, steps, title in zip(axes, [week1, week2], ['Week 1', 'Week 2']):
    colors = ['tab:green' if s >= goal else 'tab:red' for s in steps]
    ax.bar(days, steps, color=colors)
    ax.axhline(goal, color='black', linestyle='--', label=f'Goal ({goal:,} steps)')
    ax.set_title(title)
    ax.set_xlabel('Day of the week')
    ax.legend()
axes[0].set_ylabel('Steps (count)')
fig.suptitle('Daily Steps vs the 8,000-Step Goal (red = below goal)')
fig.savefig(FIG_DIR / "q23_steps_goal.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
Week 1: days meeting goal = 4, mean steps = 8142.86
Week 2: days meeting goal = 5, mean steps = 8928.57
```

![Daily steps for two weeks against the 8,000-step goal](figures/q23_steps_goal.png)

### Explanation

`sharey=True` gives both subplots the same y-axis so the bar heights can be compared directly between weeks. A list comprehension colours each bar green when it meets the goal and red when it does not, and `axhline` draws the 8000-step goal line. Week 1 had 4 days at or above the goal and a mean of 8142.86, and week 2 had 5 days and a mean of 8928.57.

**Interpret:** Yes, the user improved in week 2: one more day met the goal (5 against 4) and the average rose by about 786 steps (8142.86 to 8928.57). The improvement is modest. Week 2 still had two days below the goal (Thu 7000 and Sat 5000), and weekends remain the weak spot in both weeks.

---

## Question 24: Telling the Revenue Story

### Aim

Compute month-over-month growth with `pct_change` and annotate the best and worst months on a revenue line chart.

### Code

```python
revenue = pd.DataFrame({'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                        'revenue': [12, 15, 21, 19, 24, 22]})
revenue['growth_pct'] = (revenue['revenue'].pct_change() * 100).round(1)
print(revenue)

best = revenue.loc[revenue['growth_pct'].idxmax()]
worst = revenue.loc[revenue['growth_pct'].idxmin()]
print("\nHighest growth:", best['month'], f"{best['growth_pct']:+.1f}%")
print("Biggest drop  :", worst['month'], f"{worst['growth_pct']:+.1f}%")

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(revenue['month'], revenue['revenue'], marker='o', color='tab:blue')
for m, v in zip(revenue['month'], revenue['revenue']):
    ax.text(m, v + 0.8, str(v), ha='center')
ax.annotate(f"Best month: {best['month']} ({best['growth_pct']:+.1f}%)",
            xy=(best['month'], best['revenue']), xytext=(0.4, 24),
            arrowprops=dict(arrowstyle='->', color='green'), color='green')
ax.annotate(f"Biggest drop: {worst['month']} ({worst['growth_pct']:+.1f}%)",
            xy=(worst['month'], worst['revenue']), xytext=(3.0, 14),
            arrowprops=dict(arrowstyle='->', color='red'), color='red')
ax.set_ylim(8, 28)
ax.set_title('Revenue Grew 83% in Six Months (₹12 lakh to ₹22 lakh)')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue (₹ lakh)')
ax.grid(True, alpha=0.3)
fig.savefig(FIG_DIR / "q24_revenue_story.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Output

```
  month  revenue  growth_pct
0   Jan       12         NaN
1   Feb       15        25.0
2   Mar       21        40.0
3   Apr       19        -9.5
4   May       24        26.3
5   Jun       22        -8.3

Highest growth: Mar +40.0%
Biggest drop  : Apr -9.5%
```

![Revenue line with best and worst months annotated](figures/q24_revenue_story.png)

### Explanation

`pct_change()` gives the change from the previous month as a fraction (the first month has no value, so it is `NaN`). Multiplying by 100 gives percent. The highest growth is March (+40.0%, from 15 to 21) and the biggest drop is April (-9.5%, from 21 to 19). `ax.text` writes each value above its point, and `annotate` with `arrowprops` draws the labelled arrows. The title states the finding rather than only describing the chart.

**Interpret (for investors):** "Revenue grew from ₹12 lakh in January to ₹22 lakh in June, an increase of 83%, with a +40% jump in March and only two small dips (April, -9.5%, and June, -8.3%)."

---

## Question 25: Publication-Ready Dashboard Figure

### Aim

Draw a sorted horizontal bar chart of class averages against a target, save it as a 300-dpi PNG and confirm the file exists.

### Code

```python
subjects = ['Maths', 'Physics', 'Programming', 'Chemistry', 'English']
class_avg = [72.3, 65.1, 81.4, 58.9, 76.0]
target = 70

order = np.argsort(class_avg)                       # lowest to highest
subjects_sorted = [subjects[i] for i in order]
avg_sorted = [class_avg[i] for i in order]
colors = ['tab:red' if v < target else 'tab:blue' for v in avg_sorted]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(subjects_sorted, avg_sorted, color=colors)
ax.axvline(target, color='black', linestyle='--', label=f'Target ({target})')
for bar, v in zip(bars, avg_sorted):
    ax.text(v + 0.8, bar.get_y() + bar.get_height() / 2, f"{v:.1f}", va='center')
ax.set_xlim(0, 95)
ax.set_title('Class Average by Subject (red = below the target of 70)')
ax.set_xlabel('Class average (marks)')
ax.set_ylabel('Subject')
ax.legend(loc='lower right')

out_path = FIG_DIR / "subject_performance.png"
fig.savefig(out_path, dpi=300, bbox_inches="tight")   # save BEFORE plt.show()
plt.show()
print("Saved file exists:", out_path.exists(), "->", out_path.as_posix())
print("Subjects below target:", [s for s, v in zip(subjects_sorted, avg_sorted) if v < target])
```

### Output

```
Saved file exists: True -> task_4/figures/subject_performance.png
Subjects below target: ['Chemistry', 'Physics']
```

![Class average by subject, sorted, with target line](figures/subject_performance.png)

### Explanation

`np.argsort` gives the order from the lowest to the highest average, and the bar colours depend on whether each value is below the target. `FIG_DIR.mkdir(parents=True, exist_ok=True)` (in the setup at the top) creates `task_4/figures/` if it does not exist. `savefig(..., dpi=300, bbox_inches="tight")` writes the high-resolution file and crops the empty margins, and `out_path.exists()` confirms it was saved.

**Why the colleague's image was blank:** `plt.show()` displays the figure and then releases it. After the window closes (or in non-interactive backends), the current figure is destroyed, so a later `plt.savefig(...)` saves a new, empty figure. The correct order is to call `plt.savefig(...)` first and `plt.show()` afterwards. Saving through the figure object (`fig.savefig`) is also safe.

**Interpret:** Two subjects need attention: Chemistry (58.9) is 11.1 marks below the target and Physics (65.1) is 4.9 below it. Maths (72.3), English (76.0) and Programming (81.4) are above the target.
