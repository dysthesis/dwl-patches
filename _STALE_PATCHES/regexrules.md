### Description
Allows the use of regular expressions for window rules "app_id" and "title"

```c
static const Rule rules[] = {
    // ...
    { "kitty-htop",  NULL,       1 << 8,       0,           -1 },
    { "^kitty$",     NULL,       0,            0,           -1 },
    // ...
};
```

### Download
- [2023-10-11](https://github.com/djpohly/dwl/compare/main...wochap:regexrules.patch)

### Authors
- [wochap](https://github.com/wochap)