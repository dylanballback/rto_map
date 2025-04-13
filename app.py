from flask import Flask, render_template

app = Flask(__name__)

# RTO 2025 race legs data (same as in the previous response, condensed for brevity)
rto_2025_legs = [
    # Leg 1
    {
        "leg_number": 1,
        "distance_miles": 4.3,
        "difficulty": "Easy",
        "exchange_points": {
            "start": "J Resort's Glow Plaza, 670 W Fourth St, Reno, NV 89503",
            "end": "Dorostkar Park, 6696 Mayberry Dr., Reno, NV"
        },
        "runner_directions": "Not available due to OCR error",
        "van_directions": "Not available due to OCR error",
        "key_rules": [],
        "elevation_profile": {
            "total_gain_ft": "Not available",
            "total_loss_ft": "Not available"
        },
        "leg_description": "Starting leg in downtown Reno, heading to Dorostkar Park.",
        "map_created": 2024
    },
    # Leg 2
    {
        "leg_number": 2,
        "distance_miles": 4.40,
        "difficulty": "Moderate",
        "exchange_points": {
            "start": "Dorostkar Park, 6696 Mayberry Dr., Reno, NV",
            "end": "Interstate U-Store, 1021 Somersett Ridge Pkwy, Reno, NV"
        },
        "runner_directions": "Not available due to OCR error",
        "van_directions": "Not available due to OCR error",
        "key_rules": [],
        "elevation_profile": {
            "total_gain_ft": "Not available",
            "total_loss_ft": "Not available"
        },
        "leg_description": "Continues through Reno to Interstate U-Store.",
        "map_created": 2024
    },
    # Leg 3
    {
        "leg_number": 3,
        "distance_miles": 15.55,
        "difficulty": "Moderate",
        "exchange_points": {
            "start": "Interstate U-Store, 1021 Somersett Ridge Pkwy, Reno, NV",
            "end": "Verdi Community Library, 270 Bridge St, Verdi, NV"
        },
        "runner_directions": [
            "Run west on Somersett Ridge Pkwy for 0.2 miles.",
            "Turn right at the roundabout, run west on Old U.S. 40 with traffic for 3.5 miles through Verdi.",
            "Turn right on Trelease Ln. for 0.1 miles.",
            "Turn right on Hill Ln. for 0.9 miles.",
            "Turn right on Bridge St. for 1.0 mile, stopping at Verdi Community Library."
        ],
        "van_directions": "Drive west on Somersett Ridge Pkwy, turn right at the roundabout, head to Verdi, turn right on Bridge St, wait at the library.",
        "key_rules": [
            "Do not park in Verdi Elementary School’s lot (school in session); park at the library.",
            "Be aware of children, parents, and avoid blocking driveways or bike lanes."
        ],
        "elevation_profile": {
            "total_gain_ft": 301,
            "total_loss_ft": 224
        },
        "leg_description": "First leg leaving Reno, entering Verdi, NV.",
        "map_created": 2024
    },
    # Leg 4 (Missing details)
    {
        "leg_number": 4,
        "distance_miles": "Unknown",
        "difficulty": "Unknown",
        "exchange_points": {
            "start": "Verdi Community Library, 270 Bridge St, Verdi, NV",
            "end": "Stampede Meadows Rd and Henness Pass Rd Junction (GPS: 39.506714, -120.092120)"
        },
        "runner_directions": "Not available due to OCR error",
        "van_directions": "Not available due to OCR error",
        "key_rules": [],
        "elevation_profile": {
            "total_gain_ft": "Not available",
            "total_loss_ft": "Not available"
        },
        "leg_description": "Not available due to OCR error",
        "map_created": 2024
    },
    # Leg 5
    {
        "leg_number": 5,
        "distance_miles": 15.55,
        "difficulty": "Moderate",
        "exchange_points": {
            "start": "Stampede Meadows Rd and Henness Pass Rd Junction (GPS: 39.506714, -120.092120)",
            "end": "Boyington Mill Campground, Boyington Mill, Truckee, CA"
        },
        "runner_directions": [
            "Run south on Stampede Dam-Meadows Rd with traffic.",
            "Stop at Boyington Mill Campground."
        ],
        "van_directions": "Drive south on Stampede Dam-Meadows Rd to XP 5, passing the exchange point on the way to XP 4.",
        "key_rules": [
            "Vans should watch for tight corners on Stampede Dam-Meadows Rd and drive carefully."
        ],
        "elevation_profile": {
            "total_gain_ft": 357,
            "total_loss_ft": 752
        },
        "leg_description": "Mostly downhill, running south along Stampede Reservoir and Little Truckee River.",
        "map_created": 2024
    },
    # Leg 6
    {
        "leg_number": 6,
        "distance_miles": 5.4,
        "difficulty": "Easy",
        "exchange_points": {
            "start": "Boyington Mill Campground, Boyington Mill, Truckee, CA",
            "end": "Tahoe Forest Church, 10315 Hirschdale Rd, Truckee, CA 96161"
        },
        "runner_directions": [
            "Continue on Stampede Dam/Meadows Rd by Boca Reservoir with traffic until the Boca Dam turnoff at 4.0 miles.",
            "Continue straight down the hill, across railroad tracks.",
            "After crossing tracks, run against traffic for the rest of the leg.",
            "Cross the Truckee River, pass under I-80, stop at Glenshire Dr. intersection (1.4 miles from tracks)."
        ],
        "van_directions": "Drive south on Stampede Dam-Meadows Rd, continue onto Hirschdale Rd, cross under I-80, arrive at Tahoe Forest Church. Drive carefully due to heavy van and foot traffic.",
        "key_rules": [
            "XP 6 is private property; respect the space and do not use equipment not part of RTO.",
            "Drive slowly when leaving XP 6; follow the one-way dirt road to Hirschdale Rd.",
            "Be cautious crossing train tracks; do not cross if gates are closing."
        ],
        "elevation_profile": {
            "total_gain_ft": 198,
            "total_loss_ft": 262
        },
        "leg_description": "Passes by Boca Reservoir, continues south on Hirschdale Rd, ends at Glenshire Dr. intersection. A gathering awaits at XP 6.",
        "map_created": 2024
    },
    # Leg 7
    {
        "leg_number": 7,
        "distance_miles": 7.4,
        "difficulty": "More Challenging",
        "exchange_points": {
            "start": "Tahoe Forest Church, 10315 Hirschdale Rd, Truckee, CA 96161",
            "end": "Prosser Dam Rd (GPS: 39.369196, -120.154631)"
        },
        "runner_directions": "Not available due to OCR error",
        "van_directions": "Not available due to OCR error",
        "key_rules": [
            "Vans must remain quiet on Prosser Dam Rd (no honking, speeding, or cheering) due to a sensitive neighborhood."
        ],
        "elevation_profile": {
            "total_gain_ft": 549,
            "total_loss_ft": 314
        },
        "leg_description": "Not available due to OCR error",
        "map_created": 2024
    },
    # Legs 8 to 28 (Missing)
    *[ # Placeholder for missing legs
        {
            "leg_number": leg_num,
            "distance_miles": "Unknown",
            "difficulty": "Unknown",
            "exchange_points": {
                "start": f"XP {leg_num-1}" if leg_num == 8 else f"XP {leg_num-1} (Unknown)",
                "end": f"XP {leg_num} (Unknown)" if leg_num < 28 else "Mound House, NV (GPS: 39.228155, -119.647267)"
            },
            "runner_directions": "Not available due to missing page",
            "van_directions": "Not available due to missing page",
            "key_rules": [],
            "elevation_profile": {
                "total_gain_ft": "Not available",
                "total_loss_ft": "Not available"
            },
            "leg_description": "Not available due to missing page",
            "map_created": 2024
        } for leg_num in range(8, 29)
    ],
    # Leg 29
    {
        "leg_number": 29,
        "distance_miles": 3.4,
        "difficulty": "More Challenging",
        "exchange_points": {
            "start": "Mound House, NV (GPS: 39.228155, -119.647267)",
            "end": "Devil’s Gate, Silver City (GPS: 39.267874, -119.645084)"
        },
        "runner_directions": [
            "Run to the end of Industrial Pkwy.",
            "Turn left on State Route 341 (Comstock Hwy), run against traffic on the shoulder.",
            "Veer left on State Route 342, run against traffic.",
            "Continue through Silver City and Devil’s Gate, cross the road, and stop at the exchange point."
        ],
        "van_directions": "After Devil’s Gate, park in the chain installation area on the right; additional parking is available up the road.",
        "key_rules": [
            "From dusk to dawn, runners must wear a lighted/reflective vest, 2 blinking lights on the back, a headlamp, and extra lights."
        ],
        "elevation_profile": {
            "total_gain_ft": 511,
            "total_loss_ft": 135
        },
        "leg_description": "A big climb to Silver City, passing through Devil’s Gate, a historic rock formation marking the Storey-Lyon County boundary, used by miners in the 1860s heading to the Comstock Lode.",
        "map_created": 2024
    },
    # Leg 30
    {
        "leg_number": 30,
        "distance_miles": 3.4,
        "difficulty": "Most Difficult",
        "exchange_points": {
            "start": "Devil’s Gate, Silver City (GPS: 39.267874, -119.645084)",
            "end": "Bucket of Blood, Virginia City (GPS: 39.310530, -119.649631)"
        },
        "runner_directions": [
            "Continue on State Route 342, run against traffic.",
            "Enter Virginia City via C St., stop at the Bucket of Blood Saloon."
        ],
        "van_directions": [
            "At the 342/341 junction, turn right onto 341.",
            "Take the first left onto D St. to reach parking in Virginia City."
        ],
        "key_rules": [],
        "elevation_profile": {
            "total_gain_ft": "Not available",
            "total_loss_ft": "Not available"
        },
        "leg_description": "Not available due to OCR error",
        "map_created": 2024
    },
    # Leg 31
    {
        "leg_number": 31,
        "distance_miles": 2.6,
        "difficulty": "Most Difficult",
        "exchange_points": {
            "start": "Bucket of Blood, Virginia City (GPS: 39.310530, -119.649631)",
            "end": "Lousetown Rd (GPS: 39.339943, -119.640708)"
        },
        "runner_directions": [
            "Exit Virginia City on the main street (becomes State Route 341), run with traffic.",
            "Turn right on Lousetown Rd.",
            "Stop at the exchange point on Lousetown Rd."
        ],
        "van_directions": [
            "Leave Virginia City via D St., which merges with C St. and becomes State Route 341.",
            "Take the second entrance to Lousetown Rd., make an immediate left into a dirt pullout for parking."
        ],
        "key_rules": [
            "Runners must run with traffic on State Route 341."
        ],
        "elevation_profile": {
            "total_gain_ft": 400,
            "total_loss_ft": 154
        },
        "leg_description": "Exits Virginia City, starting the return to Reno.",
        "map_created": 2024
    },
    # Leg 32
    {
        "leg_number": 32,
        "distance_miles": 3.3,
        "difficulty": "Most Difficult",
        "exchange_points": {
            "start": "Lousetown Rd (GPS: 39.339943, -119.640708)",
            "end": "Toll Rd/Cartwright Rd Intersection (GPS: 39.369310, -119.667059)"
        },
        "runner_directions": [
            "Return to State Route 341, run with traffic.",
            "At the Toll Rd./Cartwright Rd. intersection, run 0.2 miles past to the exchange on the right."
        ],
        "van_directions": "Park beyond the exchange in the designated lot; do not park along or across the highway or on Cartwright Rd.",
        "key_rules": [
            "Vans should be cautious of runners crossing the road near XP 32.",
            "Do not park along or across the highway or on Cartwright Rd."
        ],
        "elevation_profile": {
            "total_gain_ft": 345,
            "total_loss_ft": 451
        },
        "leg_description": "Crosses Geiger Summit, continuing toward Reno.",
        "map_created": 2024
    },
    # Leg 33
    {
        "leg_number": 33,
        "distance_miles": 5.6,
        "difficulty": "More Challenging",
        "exchange_points": {
            "start": "Toll Rd/Cartwright Rd Junction (GPS: 39.369310, -119.667059)",
            "end": "Western Skies Dr./Reading St. Intersection by Brown Elementary School (GPS: 39.404297, -119.726343)"
        },
        "runner_directions": [
            "Run back against traffic on State Route 341 for 0.2 miles to Cartwright Rd., then cross the highway.",
            "Run west on the dirt portion of Toll Rd. across a meadow, then down the canyon for 3.7 miles (some steep, rocky sections).",
            "Continue on the single-lane paved road for 0.5 miles.",
            "Continue on the two-lane paved Toll Rd. for 1.9 miles (paved path on the left).",
            "Cross State Route 341 at the traffic light/crosswalk.",
            "Continue on Equestrian Rd. for 0.3 miles.",
            "Veer right onto Western Skies Dr. for 0.4 miles.",
            "Stop at the exchange at Western Skies Dr. and Reading St."
        ],
        "van_directions": [
            "Drive down State Route 341 (Geiger Grade Hwy) for 6.5 miles.",
            "Optionally, turn left on Kivett Ln., then left on Toll Rd. to a dirt pullout (furthest point allowed).",
            "Otherwise, meet the runner at XP 33."
        ],
        "key_rules": [
            "Vans must not follow runners down Toll Rd from XP 32."
        ],
        "elevation_profile": {
            "total_gain_ft": 45,
            "total_loss_ft": 1792
        },
        "leg_description": "A demanding run down Toll Rd, mostly downhill with dirt roads, returning to Reno. REMSA will be at the bottom for first aid.",
        "map_created": 2024
    },
    # Leg 34 (Missing details)
    {
        "leg_number": 34,
        "distance_miles": "Unknown",
        "difficulty": "Unknown",
        "exchange_points": {
            "start": "Western Skies Dr./Reading St. Intersection by Brown Elementary School (GPS: 39.404297, -119.726343)",
            "end": "Parkway Athletic Club, 9400 Double Diamond Pkwy, Reno, NV 89521"
        },
        "runner_directions": "Not available due to OCR error",
        "van_directions": "Not available due to OCR error",
        "key_rules": [],
        "elevation_profile": {
            "total_gain_ft": "Not available",
            "total_loss_ft": "Not available"
        },
        "leg_description": "Not available due to OCR error",
        "map_created": 2024
    },
    # Leg 35
    {
        "leg_number": 35,
        "distance_miles": 6.2,
        "difficulty": "Moderate",
        "exchange_points": {
            "start": "Parkway Athletic Club, 9400 Double Diamond Pkwy, Reno, NV 89521",
            "end": "Huffaker Elementary School, 980 Wheatland Rd, Reno, NV 89511"
        },
        "runner_directions": [
            "Run north on Double Diamond Pkwy with traffic for 0.8 miles.",
            "Turn right on Double R Blvd., run against traffic for 1.0 mile.",
            "Turn left on Longley Ln., run against traffic for 1.0 mile to South Virginia St.",
            "Carefully cross at the intersection; Longley Ln. becomes Huffaker Ln.",
            "Run west on Huffaker Ln. for 1.5 miles.",
            "Turn right on Lakeside Dr., run against traffic around Windy Hill for 1.3 miles.",
            "Turn right on Bartley Ranch Rd., cross Lakeside Dr. using the crosswalk, run 0.1 miles.",
            "Turn left on Wheatland Rd. for 0.1 miles to the exchange at Huffaker Elementary School."
        ],
        "van_directions": "Continue past the exchange, turn right into the school parking lot.",
        "key_rules": [],
        "elevation_profile": {
            "total_gain_ft": 313,
            "total_loss_ft": 182
        },
        "leg_description": "Travels through south Reno, with views on Windy Hill near the end.",
        "map_created": 2024
    },
    # Leg 36
    {
        "leg_number": 36,
        "distance_miles": 6.55,
        "difficulty": "Moderate",
        "exchange_points": {
            "start": "Huffaker Elementary School, 980 Wheatland Rd, Reno, NV 89511",
            "end": "J Resort's Glow Plaza, 670 W 4th St, Reno, NV 89503"
        },
        "runner_directions": [
            "Backtrack 0.1 miles to Bartley Ranch Rd., then 0.1 miles to Lakeside Dr.",
            "Turn right on Lakeside Dr., run with traffic for 0.4 miles to S McCarran Blvd.",
            "Cross Lakeside Dr., run against traffic for 2 miles to Plumb Ln.",
            "Cross to the north side of Plumb Ln., run with traffic for 1.5 miles to Hunter Lake Dr.",
            "Turn right on Hunter Lake Dr., run with traffic for 0.3 miles.",
            "At the 5-way intersection, turn hard right onto Charles Dr., run 0.4 miles.",
            "Turn right on Mayberry Dr. (becomes California Ave.), run with traffic on the sidewalk for 0.4 miles.",
            "Turn left on Booth St., cross to the east side, run with traffic for 0.4 miles.",
            "Cross the Truckee River via the Booth St. bridge, turn right onto the river pathway, run 0.45 miles to Ralston St./W 1st St.",
            "Turn left at the sidewalk split, cross W 1st St., head onto Ralston St.",
            "Cross to the west side of Ralston St., run north against traffic for 0.25 miles (two blocks).",
            "Turn left into the finish line at J Resort's Glow Plaza."
        ],
        "van_directions": "Park at J Resort parking lots on Ralston St. or N Arlington Ave.",
        "key_rules": [
            "No alcohol outside the festival area."
        ],
        "elevation_profile": {
            "total_gain_ft": 219,
            "total_loss_ft": 288
        },
        "leg_description": "The final leg through Reno’s city streets to the finish line festival, requiring careful navigation of traffic and crosswalks.",
        "map_created": 2024
    }
]

# Calculate total known distance
def calculate_total_distance(legs):
    total_distance = 0
    for leg in legs:
        if isinstance(leg["distance_miles"], (int, float)):
            total_distance += leg["distance_miles"]
    return total_distance

total_known_distance = calculate_total_distance(rto_2025_legs)
estimated_missing_distance = 21 * 5  # 21 missing legs (8-28), assuming 5 miles each
total_estimated_distance = total_known_distance + estimated_missing_distance

# Routes
@app.route('/')
def index():
    return render_template('index.html', 
                         total_known_distance=total_known_distance,
                         estimated_missing_distance=estimated_missing_distance,
                         total_estimated_distance=total_estimated_distance)

@app.route('/legs')
def legs():
    return render_template('legs.html', legs=rto_2025_legs)

@app.route('/leg/<int:leg_number>')
def leg_detail(leg_number):
    leg = next((leg for leg in rto_2025_legs if leg["leg_number"] == leg_number), None)
    if leg is None:
        return "Leg not found", 404
    return render_template('leg_detail.html', leg=leg)

if __name__ == '__main__':
    app.run(debug=True)