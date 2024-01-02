### Description
This patch swaps the current window (C) with the previous master (P) when zooming.
```
Original behaviour :
+-----------------+-------+
|                 |       |
|                 |       |
|                 |       |
|        P        +-------|
|                 |       |
|                 |   C   |
|                 |       |
+-----------------+-------+

+-----------------+-------+
|                 |       |
|                 |   P   |
|                 |       |
|        C        +-------|
|                 |       |
|                 |       |
|                 |       |
+-----------------+-------+

New Behaviour :
+-----------------+-------+
|                 |       |
|                 |       |
|                 |       |
|        C        +-------+
|                 |       |
|                 |   P   |
|                 |       |
+-----------------+-------+

+-----------------+-------+
|                 |       |
|                 |       |
|                 |       |
|        P        +-------+
|                 |       |
|                 |   C   |
|                 |       |
+-----------------+-------+
```

### Download
- [2023-07-28](https://github.com/djpohly/dwl/compare/main...PalanixYT:zoomswap.patch)

### Authors
- [PalanixYT](https://github.com/PalanixYT)