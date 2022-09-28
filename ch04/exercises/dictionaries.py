article = """Queen Elizabeth II's favorite pet corgis have seen a dramatic increase in sales in UK sales after her demise.

According to AFP, citing Pets4Homes, one of the UK's largest pet marketplace, it was currently seen "over ten times the volume of daily searches for corgis when compared to this time last week."

The prices asked for by registered corgi breeders have today hit a new high, with average asking prices doubling over the past three days." the pet site added.
As per Pets4Homes, the small herding dogs sell for a whopping $2,678.

Reviewed by Insider, a one-year-old Cardigan Welsh corgi was listed for $2,370 on the Pets4Homes, while two Pembroke Welsh corgis were going for $1,400 and $2,154.

Queen Elizabeth II's affection for corgis was widely known that Queen's first corgi, Susan, went along with the then-princess on her honeymoon in 1947.

While her remaining corgis, Muick and Sandy also attend her funeral at Committal Service at St George's Chapel on September 19.

Queen Elizabeth II is reported to have boasted 30 corgis over her 70-year reign."""

substitutions = {
  "corgi":"duck",
  "affection":"hate",
  "funeral":"wedding",
  "daily":"monthly",
  "Queen Elizabeth":"Donald Duck",
  "UK":"China",
  "honeymoon":"affair",
  "small":"big",
  "increase":"decrease"
}

for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)
  
  