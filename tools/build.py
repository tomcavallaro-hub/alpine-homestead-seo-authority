#!/usr/bin/env python3
"""Generate the Alpine Homestead SEO guide pages as static HTML."""
import json, os, sys, html

OUT = sys.argv[1]
BASE = "https://tomcavallaro-hub.github.io/alpine-homestead-seo-authority/"
HOME = "https://thealpinehomestead.com/"
SITE = "https://www.thealpinehomestead.com/"
BOOK = "https://www.fairly.com/listing/43075772"
UPDATED = "2026-10-24"
UPDATED_TXT = "October 24, 2026"

LODGING = {
    "@type": "LodgingBusiness",
    "@id": SITE + "#lodging",
    "name": "The Alpine Homestead",
    "url": SITE,
    "description": "Historic circa-1850 vacation rental in Olmstedville, NY near Gore Mountain with 5 bedrooms and 4 bathrooms, sleeping up to 12 guests.",
    "image": SITE + "assets/photos/aerial-house.webp",
    "address": {"@type": "PostalAddress", "streetAddress": "1314 Co Rd 29",
                "addressLocality": "Olmstedville", "addressRegion": "NY",
                "postalCode": "12857", "addressCountry": "US"},
    "numberOfRooms": 5,
    "checkinTime": "16:00",
    "checkoutTime": "10:00",
    "petsAllowed": True,
}

PAGES = []  # filled below


def page(slug, title, desc, h1, crumb, keyword, faqs, body, og_title=None):
    PAGES.append(dict(slug=slug, title=title, desc=desc, h1=h1, crumb=crumb,
                      keyword=keyword, faqs=faqs, body=body, og_title=og_title or h1))


FACTS = """<ul class="facts" aria-label="Property specifications">
  <li><b>5</b><span>Bedrooms</span></li>
  <li><b>4</b><span>Bathrooms</span></li>
  <li><b>12</b><span>Guests max</span></li>
  <li><b>1.6</b><span>Acres</span></li>
</ul>"""


def home_box(text):
    return f'<div class="home-link"><p>{text}</p></div>'


# ---------------------------------------------------------------- 1. Groups
page(
    "gore-mountain-group-vacation-rental",
    "Gore Mountain Group Vacation Rental for 12 | The Alpine Homestead™",
    "Organizing a group trip to Gore Mountain? See the bed-by-bed layout, bathroom count, parking and meal logistics for a 5-bedroom, 4-bath house in Olmstedville, NY that sleeps 12.",
    "Booking one house for a group of 12 near Gore Mountain",
    "Group stays near Gore",
    "gore mountain vacation rentals for groups",
    [("How many people can the house sleep?", "Up to 12 guests, in 5 bedrooms with 4 bathrooms."),
     ("Will 12 single adults each get their own bed?", "No. There are six beds: a King, two Queens, two Fulls and a Twin. Twelve guests means most beds are shared, so the house suits couples and families best."),
     ("How far is Gore Mountain?", "The host lists the drive at roughly 8 to 10 minutes. It is not ski-in or walking distance."),
     ("Is there room for several cars?", "Yes. The host lists off-street parking for multiple vehicles, plus trailers, snowmobiles and motorcycles.")],
    f"""
<p class="lede">The person who organizes a group trip to Gore Mountain usually ends up answering the same questions from everyone: Where do I sleep? How many bathrooms? Who's driving? This guide answers them for <a href="{HOME}">The Alpine Homestead™</a>, a circa-1850 farmhouse in Olmstedville, New York.</p>
{FACTS}
{home_box(f'Photos, the full amenity list and direct booking are on the official site: <a href="{HOME}"><strong>thealpinehomestead.com</strong></a>.')}

<h2>Beds first, headcount second</h2>
<p>Group trips fall apart over beds more often than over cost. The host publishes this layout:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Room</th><th scope="col">Beds</th><th scope="col">Works for</th></tr></thead>
<tbody>
<tr><td>Bedroom 1</td><td>King</td><td>A couple</td></tr>
<tr><td>Bedroom 2</td><td>Queen</td><td>A couple</td></tr>
<tr><td>Bedroom 3</td><td>Full</td><td>A couple, or two kids</td></tr>
<tr><td>Bedroom 4</td><td>Full</td><td>A couple, or two kids</td></tr>
<tr><td>Bedroom 5</td><td>Queen + Twin</td><td>A couple plus one, or three kids</td></tr>
</tbody></table></div>
<p>Six beds hold twelve people only when most of them share. Five couples plus two singles fits. Twelve friends who each want a bed does not. Settle room assignments before anyone pays a deposit.</p>

<h2>The bathroom math</h2>
<p>Four full bathrooms for twelve guests is three people per bathroom. That ratio is what keeps a 7 a.m. ski morning from turning into a line in the hallway,.</p>

<h2>Splitting the house fairly</h2>
<p>Rates for your dates appear only on the <a href="{BOOK}">official booking page</a>, so this guide lists no prices. Two common ways groups divide the total:</p>
<ul>
<li><strong>By room:</strong> the King and Queen rooms pay a little more than the Fulls.</li>
<li><strong>By person:</strong> simplest when the group is mostly couples.</li>
</ul>
<p>Whichever you choose, collect each share before booking. The minimum stay is 2 nights, or 3 on weekends and holidays.</p>

<h2>Cars, parking and the drive</h2>
<p>The host lists the drive to Gore Mountain at roughly 8 to 10 minutes. Plan at least two or three cars for twelve people. The property has off-street parking with space for several vehicles, plus room for trailers, snowmobiles and motorcycles.</p>

<h2>Meals for twelve</h2>
<p>The kitchen is fully equipped, and the host's list includes a dishwasher, ice maker, stand mixer, slow cooker and coffee grinder. The nearest full grocery is TOPS Markets in North Creek, which the host puts 10 to 15 minutes away. Assign one dinner per couple and the cooking stays manageable. For one night off, the host can arrange a <a href="{SITE}chef-services.html">private chef</a>, depending on the chef's schedule.</p>

<h2>When people want different things</h2>
<p>Mixed groups split up during the day. Skiers head to <a href="{SITE}gore-mountain.html">Gore Mountain</a>. Others pick from the host's <a href="{SITE}stay-play.html">Stay &amp; Play™ list</a> of local outfitters, including rail biking out of North Creek and guided outings. In the evening everyone is back at the wood stove, the foosball table or the fire pit.</p>
""")

# ---------------------------------------------------------------- 2. Weddings
page(
    "wedding-guest-lodging-gore-mountain",
    "Wedding Guest Lodging Near Gore Mountain | The Alpine Homestead™",
    "Attending or hosting a wedding near Gore Mountain? A 5-bedroom, 4-bath house in Olmstedville, NY sleeps 12. Plan where the wedding party stays, getting ready, and the weekend schedule.",
    "Where to put the wedding party for a Gore Mountain wedding",
    "Wedding guest lodging",
    "wedding guest lodging near gore mountain",
    [("Does Gore Mountain offer lodging for wedding guests?", "Gore Mountain's wedding guide says it provides referrals to local lodging and rentals; it does not list lodging of its own."),
     ("How many wedding guests can stay at The Alpine Homestead?", "Up to 12 guests, in 5 bedrooms with 4 bathrooms."),
     ("Can we hold a small wedding at the house?", "The host says the property suits micro-weddings and small celebrations. Contact the host with your dates and group size for details."),
     ("What are check-in and check-out times?", "Check-in is 4:00 PM and check-out is 10:00 AM. Plan the wedding-day schedule around those times.")],
    f"""
<p class="lede">Gore Mountain's own wedding materials describe mountaintop ceremonies reached by the gondola and receptions in the base-area Tannery hall. What they don't provide is beds. Gore refers couples to local lodging instead. If you're the couple, a parent or the maid of honor trying to keep the wedding party under one roof, <a href="{HOME}">The Alpine Homestead™</a> in Olmstedville sleeps 12.</p>
{FACTS}
{home_box(f'See the house, its wedding-weekend page and direct booking at <a href="{HOME}"><strong>The Alpine Homestead™ official site</strong></a>.')}

<h2>Who this house suits</h2>
<ul>
<li><strong>The wedding party.</strong> Bridesmaids, groomsmen or the couple's immediate families in one place, so nobody misses the hair-and-makeup start time.</li>
<li><strong>One family branch.</strong> Grandparents, siblings and kids traveling together for a wedding at Gore or elsewhere in the area.</li>
<li><strong>A micro-wedding.</strong> The host describes the 1.6-acre lawn, wraparound porch and common rooms as a setting for small ceremonies and celebrations. Ask the host directly about your plans before booking.</li>
</ul>

<h2>A wedding weekend, hour by hour</h2>
<p>Check-in is 4:00 PM and check-out is 10:00 AM. A typical three-night wedding weekend lines up like this:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">When</th><th scope="col">What happens</th><th scope="col">Plan for</th></tr></thead>
<tbody>
<tr><td>Thursday, 4 PM</td><td>Wedding party checks in</td><td>A grocery run on the way in</td></tr>
<tr><td>Friday</td><td>Rehearsal and rehearsal dinner</td><td>The host can arrange a <a href="{SITE}chef-services.html">private chef</a> to cook at the house, subject to availability</td></tr>
<tr><td>Saturday</td><td>Getting ready, ceremony, reception</td><td>Four bathrooms for twelve people getting dressed at once</td></tr>
<tr><td>Sunday morning</td><td>Recovery</td><td>The host lists yoga as a bookable morning-after option</td></tr>
<tr><td>Sunday, 10 AM</td><td>Check-out</td><td>Pack Saturday night</td></tr>
</tbody></table></div>
<p>Weekend stays have a 3-night minimum, so a Thursday-to-Sunday wedding block fits naturally. Exact rules for your dates appear on the <a href="{BOOK}">official booking page</a>.</p>

<h2>Getting everyone there and back</h2>
<p>The host lists the drive to Gore Mountain at roughly 8 to 10 minutes. Gore's base area is in North Creek. Line up sober drivers for the reception before the weekend starts. Mountain roads at night are no place to sort that out. Off-street parking has room for several vehicles.</p>

<h2>Questions to ask before you reserve</h2>
<div class="note"><ul>
<li>Are your wedding dates inside a weekend or holiday minimum-stay window?</li>
<li>Will guests share beds? The six beds are a King, two Queens, two Fulls and a Twin.</li>
<li>Are you planning any event at the house itself? Tell the host your plans and headcount up front.</li>
<li>Do you need a high chair or pack-and-play for young guests? The host lists both.</li>
</ul></div>
<p>The host's own <a href="{SITE}wedding-weekend.html">wedding and celebration weekends page</a> covers what the house offers for events.</p>
""")

# ---------------------------------------------------------------- 3. North Creek
page(
    "north-creek-adirondack-group-lodging",
    "North Creek & Adirondack Group Lodging Sleeps 12 | The Alpine Homestead™",
    "Looking for group accommodations near North Creek in the Adirondacks? How Olmstedville relates to North Creek, what's in town, and a 5-bed, 4-bath house that sleeps 12.",
    "Group accommodations near North Creek, in the Adirondack Park",
    "North Creek group lodging",
    "north creek adirondack group accommodations",
    [("Is The Alpine Homestead in North Creek?", "No. It is in Olmstedville, a hamlet in the town of Minerva, Essex County. North Creek is in the neighboring town of Johnsburg, Warren County. Both are inside the Adirondack Park."),
     ("How far is North Creek from the house?", "The host puts the TOPS grocery in North Creek about 10 to 15 minutes away."),
     ("What kinds of groups stay here?", "Family reunions, multi-family trips, friend groups and small celebrations. It sleeps up to 12 in 5 bedrooms with 4 bathrooms."),
     ("Is there Wi-Fi for remote work?", "The host lists high-speed Wi-Fi throughout the house.")],
    f"""
<p class="lede">North Creek is the hub for this corner of the Adirondacks, but most group-sized rentals sit in the hamlets around it. <a href="{HOME}">The Alpine Homestead™</a> is one of them: a 5-bedroom farmhouse in Olmstedville, a short drive north of North Creek.</p>
{FACTS}
{home_box(f'Full details, photos and direct booking: <a href="{HOME}"><strong>visit The Alpine Homestead™</strong></a>.')}

<h2>Getting the geography straight</h2>
<p>Listings blur these place names together, so here is how they fit:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Place</th><th scope="col">Town</th><th scope="col">County</th><th scope="col">Known for</th></tr></thead>
<tbody>
<tr><td>North Creek</td><td>Johnsburg</td><td>Warren</td><td>Gore Mountain, the North Creek Ski Bowl, the historic rail station</td></tr>
<tr><td>Olmstedville</td><td>Minerva</td><td>Essex</td><td>Largest hamlet in Minerva; home of The Alpine Homestead™</td></tr>
<tr><td>Minerva Lake</td><td>Minerva</td><td>Essex</td><td>A small swimming lake with a beach, which the host calls a neighbor</td></tr>
</tbody></table></div>
<p>All of it lies inside the Adirondack Park.</p>

<h2>What North Creek gives a group</h2>
<ul>
<li><strong>Gore Mountain and the Ski Bowl.</strong> Gore's original base camp, the North Creek Ski Bowl, dates to 1934 and sits near the village.</li>
<li><strong>Rail history.</strong> North Creek was the northern end of the first railroad into the Adirondacks. In 1901, Vice President Theodore Roosevelt raced from Mount Marcy to the North Creek station as President McKinley lay dying.</li>
<li><strong>Rail biking.</strong> Revolution Rail runs pedal rail-bike tours from North Creek Station; its site lists a 7-mile round-trip North Run and an 8-mile pedal-assist South Run along the Hudson. See the host's <a href="{SITE}rail-bike.html">rail biking page</a>.</li>
<li><strong>Culture on a rainy day.</strong> The North Creek Depot Museum and the Tannery Pond Community Center.</li>
<li><strong>Supplies.</strong> TOPS Markets for groceries, and restaurants including The Barking Spider on Main Street, from the host's <a href="{SITE}locals.html">local guide</a>.</li>
</ul>

<h2>Hotel rooms or one house?</h2>
<p>For a dozen people, the choice usually comes down to this:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Need</th><th scope="col">Several hotel rooms</th><th scope="col">One whole house</th></tr></thead>
<tbody>
<tr><td>Shared meals</td><td>Restaurants every night</td><td>One kitchen and one dining table</td></tr>
<tr><td>Evenings together</td><td>Someone's room, or the lobby</td><td>Living room, wood stove, porch, fire pit</td></tr>
<tr><td>Kids' bedtime</td><td>Separate rooms down a hall</td><td>Everyone under one roof</td></tr>
<tr><td>Gear and vehicles</td><td>Standard lot</td><td>Off-street parking with trailer room</td></tr>
</tbody></table></div>

<h2>Groups that fit this house</h2>
<ul>
<li><strong>Family reunions.</strong> Three generations in five bedrooms, with a playhouse and swing set for the youngest.</li>
<li><strong>Two or three families traveling together.</strong> Four bathrooms keep mornings moving.</li>
<li><strong>Small retreats.</strong> The host lists Wi-Fi throughout, a library reading room, and bookable yoga and private-chef meals.</li>
<li><strong>Snowmobile and motorcycle trips.</strong> There is parking room for trailers and bikes. See the host's <a href="{SITE}snowmobiling.html">snowmobiling page</a>.</li>
</ul>
""")

# ---------------------------------------------------------------- 4. Rafting
page(
    "hudson-river-rafting-lodging-north-creek",
    "Whitewater Rafting Lodging Near North Creek, NY | The Alpine Homestead™",
    "Rafting the Hudson River Gorge with a group? When the water is biggest, how dam-release days work, which outfitters run trips, and a 5-bed, 4-bath house nearby that sleeps 12.",
    "Lodging for a Hudson River Gorge rafting trip near North Creek",
    "Rafting lodging",
    "whitewater rafting lodging near north creek",
    [("When is the whitewater biggest on the Hudson Gorge?", "In spring, when snowmelt raises the river; the state tourism site says rafting season typically begins around the second week of April. Summer trips rely on scheduled dam releases and run gentler."),
     ("Which days do summer releases happen?", "American Whitewater lists releases from the Lake Abanakee dam on the Indian River on Tuesday, Thursday, Saturday and Sunday mornings in season. Confirm your date with your outfitter."),
     ("Is there a minimum age for rafting?", "Age and weight minimums are set by each outfitter and depend on the season and trip. Ask the outfitter before booking."),
     ("How many rafters can stay at The Alpine Homestead?", "Up to 12 guests, in 5 bedrooms with 4 bathrooms.")],
    f"""
<p class="lede">The Hudson River Gorge is one of the East's best-known whitewater runs, and trips are usually booked by groups. That leaves you with twelve wet, hungry people to house. <a href="{HOME}">The Alpine Homestead™</a> in Olmstedville is a 5-bedroom basecamp a short drive from the North Creek outfitters.</p>
{FACTS}
{home_box(f'Book the house first, then the river: <a href="{HOME}"><strong>The Alpine Homestead™ official site</strong></a>.')}

<h2>Choose your season</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Season</th><th scope="col">What the river is like</th><th scope="col">Best for</th></tr></thead>
<tbody>
<tr><td>Spring (from about mid-April)</td><td>Snowmelt brings the biggest, coldest water of the year</td><td>Experienced, adventurous adults</td></tr>
<tr><td>Summer</td><td>Scheduled dam releases; warmer and more relaxed</td><td>Mixed groups and first-timers</td></tr>
<tr><td>Fall</td><td>Quieter water, with foliage along the gorge</td><td>Scenery-minded groups</td></tr>
</tbody></table></div>
<p>The host's own <a href="{SITE}whitewater-rafting.html">rafting page</a> calls June the sweet spot.</p>

<h2>How release days work</h2>
<p>Outside spring melt, the Gorge depends on water released from the Lake Abanakee dam on the Indian River near Indian Lake. American Whitewater lists those releases on Tuesday, Thursday, Saturday and Sunday mornings, May through September. Book your trip on a release day, and confirm the schedule with your outfitter, since it can change.</p>

<h2>The trip itself</h2>
<p>North Creek Rafting Company, the host's rafting partner, lists its Hudson River Gorge day trip at 17 miles of Class III to IV water. It also offers overnight trips and a 5-mile Class I lazy-river tubing run for anyone who'd rather float. No prior rafting experience is needed for guided trips; outfitters supply a New York State licensed guide, equipment and instruction.</p>
<p>The state tourism site lists Gorge outfitters in several towns:</p>
<ul>
<li><strong>North Creek:</strong> <a href="http://www.northcreekrafting.com/">North Creek Rafting Company</a>, Whitewater Challengers, Adirondack Adventures</li>
<li><strong>North River:</strong> Adirondack River Outfitters</li>
<li><strong>Indian Lake:</strong> Adirondac Rafting Company, Adventure Sports Rafting Company</li>
<li><strong>Warrensburg:</strong> Wild Waters Outdoor Center</li>
</ul>
<p>Ask each outfitter where trips meet, since meeting points and drive times differ.</p>

<h2>Why a house beats a motel after a river day</h2>
<ul>
<li><strong>Four bathrooms</strong> for twelve people coming off the river at the same time.</li>
<li><strong>A full kitchen</strong> for one big dinner, or a <a href="{SITE}chef-services.html">private chef</a> arranged through the host.</li>
<li><strong>A fire pit</strong> for retelling the rapids. The host supplies wood for the first fire.</li>
<li><strong>Parking</strong> with room for several cars, so the group can split up for different outfitters.</li>
</ul>

<h2>Packing list for rafters</h2>
<div class="note"><ul>
<li>A full change of dry clothes and a towel to leave in the car</li>
<li>Footwear that stays on in water; ask your outfitter what they allow</li>
<li>Groceries bought on the way in; TOPS in North Creek is the nearest full grocery</li>
<li>For spring trips, ask about wetsuit or drysuit rentals before you arrive</li>
</ul></div>
""")

# ---------------------------------------------------------------- 5. Large family ski
page(
    "large-family-ski-rental-gore-mountain",
    "Large-Family Ski Vacation Rental Near Gore Mountain | The Alpine Homestead™",
    "Planning a ski week at Gore Mountain with kids, grandparents and cousins? Lessons by age, the Ski Bowl at night, baby gear, bed layout, and a 5-bedroom, 4-bath house that sleeps 12.",
    "A ski vacation near Gore Mountain for the whole extended family",
    "Family ski rentals",
    "large family ski vacation rental near gore mountain",
    [("Does Gore Mountain teach kids?", "Yes. Gore lists group lessons for children ages 4 to 12, daily lessons for ages 13 and up, private lessons for all ages, and adaptive lessons."),
     ("Is there baby gear at the house?", "The host lists a high chair and a pack-and-play."),
     ("Can we ski at night?", "Gore says all lift tickets and season passes include night access at the North Creek Ski Bowl. Check the current schedule before you go."),
     ("How many people does the house sleep?", "Up to 12 guests, in 5 bedrooms with 4 bathrooms.")],
    f"""
<p class="lede">A ski trip with toddlers, teenagers and a grandparent who'd rather read by the fire needs a different plan than a weekend with friends. Here's how a large family can run a Gore Mountain ski trip from <a href="{HOME}">The Alpine Homestead™</a>, a 5-bedroom house in Olmstedville.</p>
{FACTS}
{home_box(f'Check family-friendly details and book direct at <a href="{HOME}"><strong>thealpinehomestead.com</strong></a>.')}

<h2>Lessons for every age</h2>
<p>Gore Mountain's lessons are grouped by age:</p>
<ul class="legend" aria-label="Gore Mountain lesson types">
<li><span class="sym circle" aria-hidden="true"></span><span><strong>Children's group lessons</strong>, ages 4 to 12</span></li>
<li><span class="sym square" aria-hidden="true"></span><span><strong>Daily adult and teen lessons</strong>, ages 13 and up</span></li>
<li><span class="sym diamond" aria-hidden="true"></span><span><strong>Private lessons</strong> for any age, and <strong>adaptive lessons</strong> for skiers with disabilities, booked by phone</span></li>
</ul>
<p>Book lessons ahead of holiday weeks through <a href="https://goremountain.com/lessons-programs/">Gore's lessons page</a>, which also lists current prices.</p>

<h2>Bedroom plan for a big family</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Room</th><th scope="col">Beds</th><th scope="col">One way to assign it</th></tr></thead>
<tbody>
<tr><td>Bedroom 1</td><td>King</td><td>Grandparents</td></tr>
<tr><td>Bedroom 2</td><td>Queen</td><td>Parents, family A</td></tr>
<tr><td>Bedroom 3</td><td>Full</td><td>Parents, family B</td></tr>
<tr><td>Bedroom 4</td><td>Full</td><td>Two cousins</td></tr>
<tr><td>Bedroom 5</td><td>Queen + Twin</td><td>Three kids, or a parent and a toddler plus the pack-and-play</td></tr>
</tbody></table></div>
<p>The host lists a high chair and a pack-and-play, so the smallest guests are covered.</p>

<h2>A day that works for everyone</h2>
<ol>
<li><strong>Morning:</strong> four bathrooms for the rush, then a short drive. The host lists it at roughly 8 to 10 minutes to Gore.</li>
<li><strong>Midday:</strong> younger kids in lessons while older skiers explore. Non-skiers can try the cross-country and snowshoe trails at Gore's Nordic Center at the North Creek Ski Bowl.</li>
<li><strong>Late afternoon:</strong> naps, foosball and board games at the house.</li>
<li><strong>Evening:</strong> Gore says lift tickets include night access at the North Creek Ski Bowl, so teenagers can get a few more runs.</li>
</ol>

<h2>Gear and drying out</h2>
<p>Renting saves hauling skis for a whole family. The host's <a href="{SITE}ski-rentals.html">ski rental page</a> points to Cunningham's Ski Barn for rentals on the way to the mountain. Back at the house, the wood-burning stove is the gathering spot after a cold day.</p>

<h2>Feeding the crew on a ski week</h2>
<p>Stock up at TOPS in North Creek, which the host puts 10 to 15 minutes away, or at the larger Price Chopper in Warrensburg, about 25 minutes. A slow cooker is on the kitchen list: start dinner before the first chairlift and it's ready at the end of the day.</p>

<div class="note"><p><strong>Before you book a holiday week:</strong> weekends and holidays carry a 3-night minimum, check-out is 10:00 AM, and pets are allowed with a fee. Read the cancellation policy on the <a href="{BOOK}">booking page</a>. Popular ski weeks fill early.</p></div>
""")

# ---------------------------------------------------------------- rendering
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;700&amp;family=Source+Sans+3:wght@400;600&amp;display=swap">'


def head(title, desc, url, og_title, ld, css):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Alpine Homestead Trip Guides">
<meta property="og:title" content="{html.escape(og_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/photos/aerial-house.webp">
{FONTS}
<link rel="stylesheet" href="{css}">
<script type="application/ld+json">
{json.dumps(ld, indent=1, ensure_ascii=False)}
</script>
</head>"""


def header(prefix):
    return f"""<header class="site">
  <a href="{prefix}">Alpine Homestead Trip Guides</a>
  <a href="{HOME}">The Alpine Homestead™ official site →</a>
</header>"""


def footer(prefix):
    return f"""<footer>
<p><a href="{HOME}">The Alpine Homestead™</a> · 1314 Co Rd 29, Olmstedville, NY 12857 · <a href="{SITE}contact.html">Contact the host</a> · <a href="{BOOK}">Book direct</a></p>
<p>Property details come from the official Alpine Homestead website. Local facts are drawn from the sources linked on each page. No prices, availability or reviews are listed here; check the official booking page. Last updated {UPDATED_TXT}.</p>
</footer>"""


os.makedirs(OUT, exist_ok=True)
for p in PAGES:
    url = BASE + p["slug"] + "/"
    others = [q for q in PAGES if q is not p]
    ld = {"@context": "https://schema.org", "@graph": [
        LODGING,
        {"@type": "Article", "headline": p["h1"], "description": p["desc"],
         "about": {"@id": LODGING["@id"]}, "dateModified": UPDATED,
         "author": {"@type": "Organization", "name": "The Alpine Homestead"},
         "mainEntityOfPage": url},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trip Guides", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faqs"]]}]}
    faq_html = "\n".join(f"<dt>{html.escape(q)}</dt>\n<dd>{html.escape(a)}</dd>" for q, a in p["faqs"])
    rel = "\n".join(f'<li><a href="../{q["slug"]}/">{html.escape(q["h1"])}</a></li>' for q in others)
    doc = f"""{head(p['title'], p['desc'], url, p['og_title'], ld, '../assets/site.css')}
<body>
<div class="wrap">
{header('../')}
<nav class="crumbs" aria-label="Breadcrumb"><a href="../">Trip Guides</a> › {html.escape(p['crumb'])}</nav>
<main>
<article>
<h1>{html.escape(p['h1'])}</h1>
{p['body'].strip()}

<h2>Quick answers</h2>
<dl class="faq">
{faq_html}
</dl>

<p style="margin-top:2rem"><a class="cta" href="{HOME}">Visit The Alpine Homestead™</a></p>
</article>

<aside aria-labelledby="more">
<h2 id="more">More trip guides</h2>
<ul class="related">
{rel}
</ul>
</aside>
</main>
{footer('../')}
</div>
</body>
</html>
"""
    os.makedirs(os.path.join(OUT, p["slug"]), exist_ok=True)
    with open(os.path.join(OUT, p["slug"], "index.html"), "w") as f:
        f.write(doc)

# index
blurbs = {
 "gore-mountain-group-vacation-rental": "Bed layout, the bathroom math, splitting costs and logistics for organizers planning a group trip.",
 "wedding-guest-lodging-gore-mountain": "Housing the wedding party for a Gore Mountain or local wedding, with a weekend timeline and questions to ask.",
 "north-creek-adirondack-group-lodging": "How Olmstedville relates to North Creek, what's in town, and hotel rooms compared with one whole house.",
 "hudson-river-rafting-lodging-north-creek": "Seasons, dam-release days, outfitters by town and a rafter's packing list for the Hudson River Gorge.",
 "large-family-ski-rental-gore-mountain": "Lessons by age, night skiing at the Ski Bowl, baby gear and a bedroom plan for three generations.",
}
idx_title = "Alpine Homestead Trip Guides: Gore Mountain & North Creek"
idx_desc = "Planning guides for groups visiting Gore Mountain and North Creek, NY: group stays, wedding lodging, rafting, family ski trips and The Alpine Homestead™, a 5-bed, 4-bath home that sleeps 12."
ld = {"@context": "https://schema.org", "@graph": [
    LODGING,
    {"@type": "CollectionPage", "name": idx_title, "description": idx_desc, "url": BASE,
     "about": {"@id": LODGING["@id"]},
     "hasPart": [{"@type": "Article", "headline": p["h1"], "url": BASE + p["slug"] + "/"} for p in PAGES]}]}
cards = "\n".join(f"""<li>
<h2><a href="{p['slug']}/">{html.escape(p['h1'])}</a></h2>
<p>{blurbs[p['slug']]}</p>
</li>""" for p in PAGES)
doc = f"""{head(idx_title, idx_desc, BASE, idx_title, ld, 'assets/site.css')}
<body>
<div class="wrap">
{header('./')}
<main>
<h1>Trip guides for groups visiting Gore Mountain and North Creek</h1>
<p class="lede">Practical planning guides for the Gore Mountain and North Creek corner of the Adirondack Park, written for the person organizing the trip. Each guide covers one kind of trip and uses <a href="{HOME}">The Alpine Homestead™</a>, a circa-1850 house in Olmstedville, NY, as the home base.</p>
{FACTS}
{home_box(f'Photos, amenities and direct booking: <a href="{HOME}"><strong>thealpinehomestead.com</strong></a>.')}
<ul class="cards">
{cards}
</ul>
</main>
{footer('./')}
</div>
</body>
</html>
"""
with open(os.path.join(OUT, "index.html"), "w") as f:
    f.write(doc)

# 404
with open(os.path.join(OUT, "404.html"), "w") as f:
    f.write(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | Alpine Homestead Trip Guides</title><meta name="robots" content="noindex"><link rel="stylesheet" href="{BASE}assets/site.css"></head><body><div class="wrap"><main><h1>Page not found</h1><p>Try the <a href="{BASE}">trip guides index</a> or <a href="{HOME}">The Alpine Homestead™</a>.</p></main></div></body></html>
""")

# sitemap + robots
urls = [BASE] + [BASE + p["slug"] + "/" for p in PAGES]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("built", len(PAGES), "pages")
