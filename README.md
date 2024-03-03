Imagine you are in charge of a food bank and it’s your responsibility to ensure that people are receiving a healthy and balanced meal. 
However, you have received a truckload of pickles, but you never receive fresh produce. Depending on their location, food banks around 
the country may have a surplus of certain food items, while lacking others. For example, it’s harder for Alaska to get hold of produce 
from other states. A meal without fresh produce is not a balanced meal, and even then, much of the donations they receive will become 
food waste that contributes to global hunger and global warming. So, what if there was a system that allowed food banks to trade their 
surplus inventory for the excess food items of another food bank? That is exactly what our website Plated allows for, serving as the 
connection between these food banks.

In a 2017 podcast episode of NPR’s Planet Money, the idea of a Free Food Market was brought up: it was a market where food banks would 
receive fake money based on how many people they feed to bid for items from Feeding America. This change in the way Feeding America 
distributes their food to different food pantries all over the country sprouted from a common issue food banks faced: not getting enough 
of food that they needed. For example, Susannah Morgan ran a food bank in Alaska and would rarely get large donations from Feeding America 
due to high transportation costs, although she had her own solution to that, and when she did get a big donation, it was a truckload of 
5-gallon buckets of pickles because it is well-preserved. On the other hand, a food bank in Idaho gets tons of potatoes from Feeding America, 
when there were already more than enough potatoes supplied by local farmers. 

We decided that instead of having this fake food bank economy, which brings along doubts of whether the smaller food banks with less monetary 
support would benefit from the program compared to existing larger and wealthier food pantries, we would set up a cost-free solution to this 
problem: a platform for food banks to trade surplus inventory for food items that they truly want that another food bank has in surplus.

Our website allows food bank managers to input information about their food distribution organization (name, address, and contact information) 
as well as the food they have in surplus they would like to trade and the food they want to obtain through trading. Then, food managers can 
browse (on our Locate page) what foods other food banks have listed as surplus items, gaining insight about the quantity in excess, the 
expiration date, and any other pertinent information to see if there is anything that matches their needs. They can also explore by location 
through interacting with the map at the bottom of the Locate page, showing the locations of listed food banks and the food they have in excess. 
They can then reach out to the other food banks and propose a trade offer, allowing food banks to mutually benefit from the transaction 
without incurring any additional costs to secure the foods required to allow food banks to serve well-balanced meals to their communities. 

We used Python to build the algorithms required for the input form to build and access the database built through SQLite and employed Flask 
to map the form submit function to a template output of the form contents. HTML and CSS was used for the front-end development of the individual 
webpages, implementing interactive features like the carousel and routing the pages within the website. We included Javascript when connecting 
the Google Maps Static Maps via Google Cloud API.

Going forward, we would like to implement a log-in page to allow food banks to update their inventory surplus items and the items that they 
are searching for on the website as their circumstances change. Additionally, we would like to implement a verification system to authenticate 
the user’s food bank and their surplus claims. We would also like to improve our current Locate page, incorporating new carousel slides as 
new entries are inputted to the system. As our number of users increases, we would like to introduce a search function with advanced filters 
to allow for quick navigation to the food items a user is looking for. In addition, we look towards implementing a trade request system within 
the website to allow for ease of communication between food banks, eliminating the hassle of external communication through phone or email. 
As an initiative, we would like to expand our network system beyond the Southern California region, allowing for a larger variety of the food 
items listed on the website and for more people to be able to access healthy, balanced meals through their local food distribution centers.
