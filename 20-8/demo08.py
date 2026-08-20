cp={
    "bang":44,
    "chennai":45,
    "hyd":543,
    "pune":245
}
lc={city:population for city,population in cp.items() if population<50} 
print(lc)

