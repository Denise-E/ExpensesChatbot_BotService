expense_examples = [
    {"input": "Hey, how are you? 20 bucks",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "Today is a nice day to eat burgers",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "20 dollars because you're a good person",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "I'd like to buy a new phone",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "I have 30,000 dollars in my account",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "The other day I saw a t-shirt that cost 10,000",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "I want to buy a pizza but it costs 60 dollars",
     "expected": {"is_expense": False, "amount": None, "category": None, "description": None}},
    {"input": "I spend 10 dollars at the cinema today",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Entertainment", "description": "Cinema"}},
    {"input": "Bought a video game on sale for 5 bucks",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Entertainment", "description": "Video game"}},
    {"input": "Subscribed to Netflix for 15 dollars",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Entertainment",
                  "description": "Netflix subscription"}},
    {"input": "Went to a concert because I got tickets for just 1 dollar",
     "expected": {"is_expense": True, "amount": "1.0", "category": "Entertainment", "description": "Concert"}},
    {"input": "I paid for a Spotify Premium subscription, is 5 bucks the first month",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Entertainment",
                  "description": "Spotify premium subscription"}},
    {"input": "Bought board games for game night for just3 dollars",
     "expected": {"is_expense": True, "amount": "3.0", "category": "Entertainment", "description": "Board games"}},
    {"input": "Paid to enter the amusement park, it costs 5 cents",
     "expected": {"is_expense": True, "amount": "0.05", "category": "Entertainment", "description": "Amusement park"}},
    {"input": "Rented a movie online for 20 bucks",
     "expected": {"is_expense": True, "amount": "20.0", "category": "Entertainment",
                  "description": "Online movie rental"}},
    {"input": "Went bowling and paid for two rounds 10 bucks",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Entertainment", "description": "Bowling"}},
    {"input": "I paid for Netflix and Spotify yesterday, it costs me a hundred bucks",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Entertainment",
                  "description": "Netflix and spotify"}},
    {"input": "I bought a 30 bucks steak with potatoes",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Food", "description": "Steak with potatoes"}},
    {"input": "I spent 10 dollars on lunch at the cafe",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Food", "description": "Lunch at cafe"}},
    {"input": "Got sushi delivered for dinner for 80 dollars",
     "expected": {"is_expense": True, "amount": "80.0", "category": "Food", "description": "Sushi delivery"}},
    {"input": "Bought groceries for the week, cost around 80",
     "expected": {"is_expense": True, "amount": "80.0", "category": "Food", "description": "Groceries"}},
    {"input": "I ordered pizza last night for 12 dollars",
     "expected": {"is_expense": True, "amount": "12.0", "category": "Food", "description": "Pizza"}},
    {"input": "I had breakfast at Starbucks, I paid 12",
     "expected": {"is_expense": True, "amount": "12.0", "category": "Food", "description": "Breakfast at Starbucks"}},
    {"input": "Bought snacks and soda at the gas station, I spend 15 bucks",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Food", "description": "Snacks and soda"}},
    {"input": "Cooked pasta but had to buy the ingredients today. It was 8 dollars",
     "expected": {"is_expense": True, "amount": "8.0", "category": "Food", "description": "Pasta ingredients"}},
    {"input": "Spent 6 on a smoothie after the gym",
     "expected": {"is_expense": True, "amount": "6.0", "category": "Food", "description": "Smoothie"}},
    {"input": "I bought chocolates and ice cream today all for 10 bucks",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Food", "description": "Chocolates and ice cream"}},
    {"input": "I bought a Coca-Cola today for 10 bucks",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Food", "description": "Coca-Cola"}},
    {"input": "I paid 25 dollars for a hamburger",
     "expected": {"is_expense": True, "amount": "25.0", "category": "Food", "description": "Hamburger"}},
    {"input": "I spent a lot at the supermarket, around 300",
     "expected": {"is_expense": True, "amount": "300.0", "category": "Food", "description": "Supermarket"}},
    {"input": "I paid 1200 for this month’s rent",
     "expected": {"is_expense": True, "amount": "1200.0", "category": "Housing", "description": "Monthly rent"}},
    {
        "input": "Bought some new curtains for the living room, it costs around 50 dollars. I don't know if it was expensive or not",
        "expected": {"is_expense": True, "amount": "50.0", "category": "Housing",
                     "description": "Curtains for living room"}},
    {"input": "I hired a plumber to fix a leaking pipe at home, I paid him 30 dollars",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Housing", "description": "Plumber service"}},
    {"input": "Paid 200 dollars for home insurance",
     "expected": {"is_expense": True, "amount": "200.0", "category": "Insurance", "description": "Home insurance"}},
    {"input": "I got a new set of keys made for my apartment for just 5 dollars",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Housing", "description": "New apartment keys"}},
    {"input": "Spent 85 bucks on home cleaning service",
     "expected": {"is_expense": True, "amount": "85.0", "category": "Housing", "description": "Home cleaning service"}},
    {"input": "Purchased a new lamp for the bedroom for 8 dollars at a garage sale",
     "expected": {"is_expense": True, "amount": "8.0", "category": "Housing", "description": "Lamp for bedroom"}},
    {"input": "Had the air conditioner repaired at home for 40 bucks",
     "expected": {"is_expense": True, "amount": "40.0", "category": "Housing",
                  "description": "Air conditioner repair"}},
    {"input": "I bought paint for the walls of the house, It cost me 11",
     "expected": {"is_expense": True, "amount": "11.0", "category": "Housing", "description": "Wall paint"}},
    {"input": "Renewed my home lease with a fee of 10 dollars",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Housing", "description": "Lease renewal fee"}},
    {"input": "I paid 1500 for the rent today",
     "expected": {"is_expense": True, "amount": "1500.0", "category": "Housing", "description": "Monthly rent"}},
    {"input": "I spent 50 bucks on gas today",
     "expected": {"is_expense": True, "amount": "50.0", "category": "Transportation", "description": "Gas"}},
    {"input": "I paid 2.75 for the subway ticket",
     "expected": {"is_expense": True, "amount": "2.75", "category": "Transportation", "description": "Subway ticket"}},
    {"input": "I ordered an Uber to go to work, I paid 12.75 fot it",
     "expected": {"is_expense": True, "amount": "12.75", "category": "Transportation", "description": "Uber to work"}},
    {"input": "Bought a monthly bus pass for 100 dollars",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Transportation",
                  "description": "Monthly bus pass"}},
    {"input": "Paid 10 dollars for parking downtown",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Transportation",
                  "description": "Parking downtown"}},
    {"input": "My car needed an oil change, cost me 75",
     "expected": {"is_expense": True, "amount": "75.0", "category": "Transportation", "description": "Car oil change"}},
    {"input": "I took a taxi to the airport for 30 bucks",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Transportation",
                  "description": "Taxi to the airport"}},
    {"input": "I booked a train to another city, it was really cheap it only costs me 3 dollars",
     "expected": {"is_expense": True, "amount": "3.0", "category": "Transportation", "description": "Train ticket"}},
    {"input": "Paid toll fees during a road trip, It costs me a 100 total",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Transportation", "description": "Toll fees"}},
    {"input": "30 bucks a new tire for my car",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Transportation", "description": "New tire"}},
    {"input": "90 dollars electricity bill",
     "expected": {"is_expense": True, "amount": "90.0", "category": "Utilities", "description": "Electricity bill"}},
    {"input": "cost me 60 my internet bill",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Utilities", "description": "Internet bill"}},
    {"input": "I paid for water services. 20. ",
     "expected": {"is_expense": True, "amount": "20.0", "category": "Utilities", "description": "Water services"}},
    {"input": "Renewed my phone plan. 15 bucks.",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Utilities", "description": "Phone plan renewal"}},
    {"input": "120 bucks. Gas and heating",
     "expected": {"is_expense": True, "amount": "120.0", "category": "Housing", "description": "Gas and heating"}},
    {"input": "Extra mobile data for 10 dollars",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Utilities", "description": "Extra mobile data"}},
    {"input": "I paid the utility deposit for the apartment. 150 dollars.",
     "expected": {"is_expense": True, "amount": "150.0", "category": "Utilities", "description": "Utility deposit"}},
    {"input": "Paid for garbage collection services, 10 this month",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Housing", "description": "Garbage collection"}},
    {"input": "Settled my sewerage charges today. It was 30 bucks",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Utilities", "description": "Sewerage charges"}},
    {"input": "Utility monitoring app subscription 12 dollars",
     "expected": {"is_expense": True, "amount": "12.0", "category": "Utilities",
                  "description": "Utility app subscription"}},
    {"input": "Paid 300 dollars for my health insurance",
     "expected": {"is_expense": True, "amount": "300.0", "category": "Insurance", "description": "Health insurance"}},
    {"input": "Travel insurance before my trip, 35 bucks",
     "expected": {"is_expense": True, "amount": "35.0", "category": "Insurance", "description": "Travel insurance"}},
    {"input": "My pet insurance costs 45",
     "expected": {"is_expense": True, "amount": "45.0", "category": "Insurance", "description": "Pet insurance"}},
    {"input": "30 bucks for dental insurance today",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Insurance", "description": "Dental insurance"}},
    {"input": "100 dollars life insurance coverage",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Insurance", "description": "Life insurance"}},
    {"input": "I paid for renter's insurance 60 bucks",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Insurance", "description": "Renter's insurance"}},
    {"input": "130 dollars home insurance",
     "expected": {"is_expense": True, "amount": "130.0", "category": "Insurance", "description": "Home insurance"}},
    {"input": "Insurance against theft 60 dollars",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Insurance", "description": "Theft insurance"}},
    {"input": "Paid for extra insurance on my new phone, 30 bucks",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Insurance", "description": "Phone insurance"}},
    {"input": "Some medicine at the pharmacy, 46 dollars",
     "expected": {"is_expense": True, "amount": "46.0", "category": "Medical/Healthcare", "description": "Medicine"}},
    {"input": "I paid 60 for a dentist appointment",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Medical/Healthcare",
                  "description": "Dentist appointment"}},
    {"input": "Went to the doctor, consultation cost 100",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Medical/Healthcare",
                  "description": "Doctor consultation"}},
    {"input": "Paid for a COVID-19 test 10 bucks",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Medical/Healthcare",
                  "description": "COVID-19 test"}},
    {"input": "I got my eyes checked today, cost 40",
     "expected": {"is_expense": True, "amount": "40.0", "category": "Medical/Healthcare", "description": "Eye check"}},
    {"input": "I bought vitamins and supplements, 30 dollars",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Medical/Healthcare",
                  "description": "Vitamins and supplements"}},
    {"input": "I had therapy today, it cost 80",
     "expected": {"is_expense": True, "amount": "80.0", "category": "Medical/Healthcare", "description": "Therapy"}},
    {"input": "Got a prescription refilled, 14 bucks",
     "expected": {"is_expense": True, "amount": "14.0", "category": "Medical/Healthcare",
                  "description": "Prescription refill"}},
    {"input": "Paid for physical therapy session, spent 30",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Medical/Healthcare",
                  "description": "Physical therapy session"}},
    {"input": "Had a blood test done at the clinic for 10 bucks",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Medical/Healthcare", "description": "Blood test"}},
    {"input": "I transferred 100 bucks to my savings account",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Savings", "description": "Savings transfer"}},
    {"input": "I invested in a savings bond 400 dollars",
     "expected": {"is_expense": True, "amount": "400.0", "category": "Savings",
                  "description": "Savings bond investment"}},
    {"input": "Put 50 dollars aside for an emergency fund",
     "expected": {"is_expense": True, "amount": "50.0", "category": "Savings", "description": "Emergency fund"}},
    {"input": "Sent money to my retirement fund, 3000 bucks",
     "expected": {"is_expense": True, "amount": "3000.0", "category": "Savings", "description": "Retirement fund"}},
    {"input": "Spent 200 this month by eating out",
     "expected": {"is_expense": True, "amount": "200.0", "category": "Food", "description": "Eating out"}},
    {"input": "30 bucks, bought government savings certificates",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Savings",
                  "description": "Government savings certificates"}},
    {"input": "500 dollars, deposit into my investment account",
     "expected": {"is_expense": True, "amount": "500.0", "category": "Savings",
                  "description": "Investment account deposit"}},
    {"input": "500 dollars deposit today",
     "expected": {"is_expense": True, "amount": "500.0", "category": "Savings", "description": "Deposit"}},
    {"input": "Moved 1500 bucks to a high-yield savings account",
     "expected": {"is_expense": True, "amount": "1500.0", "category": "Savings",
                  "description": "High-yield savings account"}},
    {"input": "I paid off 200 of my credit card",
     "expected": {"is_expense": True, "amount": "200.0", "category": "Debt", "description": "Credit card payment"}},
    {"input": "Sent 500 to repay my student loan",
     "expected": {"is_expense": True, "amount": "500.0", "category": "Debt", "description": "Student loan repayment"}},
    {"input": "Made a mortgage payment today for 600 dollars",
     "expected": {"is_expense": True, "amount": "600.0", "category": "Housing", "description": "Mortgage payment"}},
    {"input": "Paid an installment on my car loan, 180 bucks",
     "expected": {"is_expense": True, "amount": "180.0", "category": "Debt", "description": "Car loan installment"}},
    {"input": "Settled a small personal loan from a friend, 150 dollars",
     "expected": {"is_expense": True, "amount": "150.0", "category": "Debt", "description": "Personal loan repayment"}},
    {"input": "Paid off my store credit account, 400 dollars",
     "expected": {"is_expense": True, "amount": "400.0", "category": "Debt", "description": "Store credit account"}},
    {"input": "Transferred funds to pay back debt, 600 dollars",
     "expected": {"is_expense": True, "amount": "600.0", "category": "Debt", "description": "Debt repayment"}},
    {"input": "600 dollars. I made a payment toward my loan principal",
     "expected": {"is_expense": True, "amount": "600.0", "category": "Debt", "description": "Loan principal payment"}},
    {"input": "Covered late fees on a loan. 300 bucks.",
     "expected": {"is_expense": True, "amount": "300.0", "category": "Debt", "description": "Loan late fees"}},
    {"input": "Sent a 300 dollars payment to my buy now pay later plan",
     "expected": {"is_expense": True, "amount": "300.0", "category": "Debt", "description": "Buy now pay later plan"}},
    {"input": "I paid 100 bucks for my online course subscription",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Education",
                  "description": "Online course subscription"}},
    {"input": "Bought new textbooks for school, it costs 80 dollars",
     "expected": {"is_expense": True, "amount": "80.0", "category": "Education",
                  "description": "Textbooks for school"}},
    {"input": "I enrolled in a programming class for just 15",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Education", "description": "Programming class"}},
    {"input": "Paid 100 for an educational webinar",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Education",
                  "description": "Educational webinar"}},
    {"input": "Bought school supplies today, 45 dollars",
     "expected": {"is_expense": True, "amount": "45.0", "category": "Education", "description": "School supplies"}},
    {"input": "I registered for a university class, 200 bucks",
     "expected": {"is_expense": True, "amount": "200.0", "category": "Education",
                  "description": "University class registration"}},
    {"input": "Paid tuition for the next semester, total 300 dollars",
     "expected": {"is_expense": True, "amount": "300.0", "category": "Education",
                  "description": "Tuition for next semester"}},
    {"input": "Signed up for language lessons for 30 dollars",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Education", "description": "Language lessons"}},
    {"input": "Bought notebooks and pens at the bookstore, costs me 350 dollars",
     "expected": {"is_expense": True, "amount": "350.0", "category": "Education", "description": "Notebooks and pens"}},
    {"input": "60 bucks for a certification exam",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Education", "description": "Certification exam"}},
    {"input": "I donated 25 to a charity",
     "expected": {"is_expense": True, "amount": "25.0", "category": "Donations", "description": "Charity donation"}},
    {"input": "I gave 10 bucks to a street musician",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Donations", "description": "Street musician"}},
    {"input": "I paid for a new passport photo, just 5 dollars",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Other", "description": "Passport photo"}},
    {"input": "Bought a gift for a friend for 30 bucks",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Gifts", "description": "Gift for a friend"}},
    {"input": "40 bucks, for a fine at the library",
     "expected": {"is_expense": True, "amount": "40.0", "category": "Other", "description": "Library fine"}},
    {"input": "10 bucks, lottery ticket",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Entertainment", "description": "Lottery ticket"}},
    {"input": "30 dollars on random items at the dollar store",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Other", "description": "Random items"}},
    {"input": "20 dollars fee to get a document notarized",
     "expected": {"is_expense": True, "amount": "20.0", "category": "Other", "description": "Document notarization"}},
    {"input": "80 bucks backpack even though I didn't need it",
     "expected": {"is_expense": True, "amount": "80.0", "category": "Shopping", "description": "Backpack"}},
    {"input": "Spent 5 bucks on a mystery box at the fair",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Entertainment",
                  "description": "Mystery box at fair"}},
    {"input": "Spent 120 dollars on clothes at the mall",
     "expected": {"is_expense": True, "amount": "120.0", "category": "Shopping", "description": "Clothes at mall"}},
    {"input": "Bought some gadgets online, total 85 bucks",
     "expected": {"is_expense": True, "amount": "85.0", "category": "Shopping", "description": "Online gadgets"}},
    {"input": "Got new headphones for 60 dollars",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Shopping", "description": "Headphones"}},
    {"input": "Spent 45 on a skincare set",
     "expected": {"is_expense": True, "amount": "45.0", "category": "Shopping", "description": "Skincare set"}},
    {"input": "Bought three books for 30 bucks",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Education", "description": "Three books"}},
    {"input": "Picked up a couple of toys for 25",
     "expected": {"is_expense": True, "amount": "25.0", "category": "Shopping", "description": "Toys"}},
    {"input": "Grabbed some home decor items, 50 dollars total",
     "expected": {"is_expense": True, "amount": "50.0", "category": "Shopping", "description": "Home decor items"}},
    {"input": "100 bucks on Black Friday deals",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Shopping", "description": "Black Friday deals"}},
    {"input": "Bought a pair of shoes, 75 dollars",
     "expected": {"is_expense": True, "amount": "75.0", "category": "Shopping", "description": "Shoes"}},
    {"input": "Bought a new phone case 10 bucks",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Other", "description": "Phone case"}},
    {"input": "Bought a birthday present for my sister, 40 dollars",
     "expected": {"is_expense": True, "amount": "40.0", "category": "Gifts",
                  "description": "Birthday present for sister"}},
    {"input": "Got a wedding gift for a friend, 100 bucks",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Gifts",
                  "description": "Wedding gift for friend"}},
    {"input": "Spent 20 on a Father's Day card and chocolates",
     "expected": {"is_expense": True, "amount": "20.0", "category": "Gifts",
                  "description": "Father's Day card and chocolates"}},
    {"input": "Bought toys for my nephew’s birthday, 35 dollars",
     "expected": {"is_expense": True, "amount": "35.0", "category": "Gifts",
                  "description": "Toys for nephew’s birthday"}},
    {"input": "Sent flowers to my mom, cost me 50 bucks",
     "expected": {"is_expense": True, "amount": "50.0", "category": "Gifts", "description": "Flowers for mom"}},
    {"input": "Purchased a Christmas gift, 60 dollars",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Gifts", "description": "Christmas gift"}},
    {"input": "Gifted a book to my mentor, 15 bucks",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Gifts", "description": "Book for mentor"}},
    {"input": "Got a souvenir for a friend while traveling, 10 dollars",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Gifts", "description": "Souvenir for friend"}},
    {"input": "Gave my colleague a going-away gift, 25",
     "expected": {"is_expense": True, "amount": "25.0", "category": "Gifts",
                  "description": "Going-away gift for colleague"}},
    {"input": "Bought an anniversary present, 80 bucks",
     "expected": {"is_expense": True, "amount": "80.0", "category": "Gifts", "description": "Anniversary present"}},
    {"input": "Donated 50 dollars to the Red Cross",
     "expected": {"is_expense": True, "amount": "50.0", "category": "Donations", "description": "Red Cross donation"}},
    {"input": "Gave 20 bucks to a local animal shelter",
     "expected": {"is_expense": True, "amount": "20.0", "category": "Donations",
                  "description": "Animal shelter donation"}},
    {"input": "I supported a GoFundMe with 15 dollars",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Donations", "description": "GoFundMe support"}},
    {"input": "Donated 100 dollars to support cancer research",
     "expected": {"is_expense": True, "amount": "100.0", "category": "Donations",
                  "description": "Cancer research donation"}},
    {"input": "Gave 5 bucks to a homeless person",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Donations", "description": "Homeless person"}},
    {"input": "Dropped 10 dollars into the church collection",
     "expected": {"is_expense": True, "amount": "10.0", "category": "Donations", "description": "Church collection"}},
    {"input": "Contributed 25 to a non-profit for education",
     "expected": {"is_expense": True, "amount": "25.0", "category": "Donations",
                  "description": "Non-profit for education"}},
    {"input": "Sent 30 to an online fundraiser for flood victims",
     "expected": {"is_expense": True, "amount": "30.0", "category": "Donations",
                  "description": "Flood victims fundraiser"}},
    {"input": "Pledged 60 bucks to a charity marathon",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Donations", "description": "Charity marathon"}},
    {"input": "I gave money to a street artist, 5 bucks",
     "expected": {"is_expense": True, "amount": "5.0", "category": "Other", "description": "Street artist"}},
    {"input": "Paid 20 bucks for document translation",
     "expected": {"is_expense": True, "amount": "20.0", "category": "Other", "description": "Document translation"}},
    {"input": "Got my passport photo printed, cost me 8 dollars",
     "expected": {"is_expense": True, "amount": "8.0", "category": "Other", "description": "Passport photo printed"}},
    {"input": "Spent 15 on mailing documents via express post",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Other", "description": "Mailing documents"}},
    {"input": "Notarization of legal papers, 25 dollars",
     "expected": {"is_expense": True, "amount": "25.0", "category": "Other",
                  "description": "Notarization of legal papers"}},
    {"input": "Spent 60 on visa application fees",
     "expected": {"is_expense": True, "amount": "60.0", "category": "Other", "description": "Visa application fees"}},
    {"input": "Paid 18 bucks for a copy of my birth certificate",
     "expected": {"is_expense": True, "amount": "18.0", "category": "Other", "description": "Birth certificate copy"}},
    {"input": "15 bucks on a replacement key for my mailbox",
     "expected": {"is_expense": True, "amount": "15.0", "category": "Housing",
                  "description": "Mailbox key replacement"}},
]
