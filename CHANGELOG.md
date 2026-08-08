# Changelog


## [1.0.0] - 2026-08-08

### Added
- connected to postgresql and loaded cleaned sales dataset into Power BI.
- Created a star schema consisting of:
  - Dim_Date
- Built a dedicated Date table for time intelligence.
- Created DAX measures:
  - Total Revenue
  - Total Orders
  - Average Order Value (AOV)
  - Unique Customers
  - Revenue per Customer
  - Orders per Customer
  - Revenue Growth %
  - YTD Revenue
  - MTD Revenue
  - QTD Revenue
- Built Executive Dashboard.
- Added slicers for:
  - Items
  

### Fixed
- Fixed inconsistent date format.
- Corrected model relationships.

### Documentation
- Added README.
- Added Business Questions documentation.
- Added dashboard screenshots.



## Lessons Learned

Through this project I learned:

- The importance of investigating data before cleaning it.
- How to build a star schema in Power BI.
- How to write DAX measures for business reporting.
- Why documenting data quality decisions is essential.
- How to design dashboards that answer business questions rather than simply display data.

