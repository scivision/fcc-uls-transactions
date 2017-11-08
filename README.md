# fcc-uls-transactions
parse FCC ULS transactions data (daily or all) text HS.dat et al

## Example for GMRS

![GMRS histogram](data/gmrs.eps)

```sh
mkdir -p data/a_gmrs
cd data/a_gmrs
wget http://wireless.fcc.gov/uls/data/complete/a_gmrs.zip
unzip a_gmrs.zip
```

## HS.dat codes
[FCC Transaction filename key](http://wireless.fcc.gov/uls/documentation/pa_intro24.pdf)

[FCC Transaction application codes](http://wireless.fcc.gov/uls/releases/d992205c.pdf)

New license order of transactions:

code | Description
------|-------------------
RECNE  |   New App Received
RDLCOM  |  Review completed
FVPCNF  |  Payment Confirmed
RDLCOM |   Review completed
APGRT   |  App Granted
AUTHPR   | Auth Printed


APGRT: Application Granted
AUTHGE: Authorization generated (not used after 1998 ?)


## Download data

[Entire history of FCC (back to late 1990s)](http://wireless.fcc.gov/uls/index.htm?job=transaction&page=weekly)

[GMRS applications](http://wireless.fcc.gov/uls/data/complete/a_gmrs.zip)
