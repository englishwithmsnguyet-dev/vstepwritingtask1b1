const studentEssay = `Dear Emily,
Thank for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.
Firstly, you should stay in hotel in the city center because it’s very convenient for travelling. Many famous places are also located near this area. Moreover, the prices are quite reasonable.
Secondly, it would be a good idea to try some traditional Vietnamese dishes such as lau mam, banh cong, and banh tet la cam. These dishes are very popular and delicious. Both locals and tourists enjoy them.
Next, if I were you, I would visit some famous places in Can Tho such as Ninh Kieu way, Cai Rang Floating Market, and My Khanh Tourist Village. These places are very beautiful and interesting. Besides, you can better understand the cultural of Can Tho.
Finally, remember to wear light and comfortable clothes because the weather in Can Tho can be very pleasant in December and an ideal time for tourism. For example, you can wear Ba Ba shirt. Don't forget to bring conical hat.
I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.
Best wishes,`;

console.log("1. Thank for:", /\bThank\s+for\b/i.test(studentEssay));
console.log("2. stay in hotel:", /\bstay\s+(in|at)\s+(hotel|homestay)\b/i.test(studentEssay));
console.log("3. wear Ba Ba shirt / conical hat:", /\b(wear|bring|take|buy)\s+(ba\s*ba\s+shirt|shirt|conical\s+hat|jacket|hat|umbrella|camera)\b/i.test(studentEssay));
console.log("4. the cultural of:", /\bthe\s+cultural\s+of\b/i.test(studentEssay));
console.log("5. Ninh Kieu way:", /\bNinh\s+Kieu\s+way\b/i.test(studentEssay));
