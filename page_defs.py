"""Page definitions. Edit copy and hero configuration here, then rebuild."""

# Hotspot coordinates are percentages of the u1-full-accessories image box.
ACC = "u1-full-accessories"
ACC_ALT = "Volty U-1 fitted with the full accessory set"

SPOTS = [
    dict(x="12%", y="31%", k="01 / Front",
         t="Front Cargo Rack",
         d="Heavy duty front platform for bulky parcels and insulated food bags. Load sits over the steering axis, so a full box does not fight the bars.",
         m="Bolt-on, no frame modification"),
    dict(x="35%", y="32%", k="02 / Mid",
         t="Mid Cargo Rail",
         d="Rails above the frame spine for stacked boxes and secured cargo. Keeps mass low and centered instead of hanging off the tail.",
         m="Rated for stacked parcel loads"),
    dict(x="75%", y="30%", k="03 / Rear",
         t="Rear Cargo Basket",
         d="Mesh basket integrated into the frame, not an add-on clamp. Rated for real cargo or a passenger, and it comes off in minutes.",
         m="Part of the frame, not an accessory clamp"),
    dict(x="92%", y="49%", k="04 / Side",
         t="Side Load Decks",
         d="Full length side decks for long or awkward freight: water, gas cylinders, construction material, anything a scooter cannot take.",
         m="Full length, both sides"),
    dict(x="33%", y="56%", k="05 / Energy",
         t="Swappable Battery Bay",
         d="One pack for nimble urban ride hailing, two for heavy long distance logistics. Same bay, same chassis, no vendor lock in.",
         m="Under 2 min swap, multi-BaaS"),
    dict(x="74%", y="74%", k="06 / Service",
         t="Exposed Drivetrain",
         d="Exposed chain, bolt-on panels, standard suspension. Any mechanic on any street can keep it running. No dealer, no special tool, no waiting.",
         m="~4 days offline a year vs ~24 on gas"),
]

PAGES = [
    # ---------------------------------------------------------------- index
    dict(
        slug="index",
        title="VOLTY U-1 | A High-Performance, Modular Electric Utility Motorcycle",
        desc="Volty U-1: Vietnam's cross-compatible battery-swapping electric utility motorcycle for delivery and ride-hailing fleets. 195 km max range, 200 kg payload, swaps in under 2 minutes.",
        hero=None,   # index keeps its own existing hero
    ),

    dict(
        slug="vision",
        title="VOLTY U-1 | Vision",
        desc="Why a utility first electric motorcycle platform, and why nobody else in Vietnam is building one.",
        crumb="Vision",
        h1="Built for work. <em>Not commuting.</em>",
        lead="Most electric two wheelers chase lifestyle buyers. We build for the rider who covers 200 km a day, six days a week, and judges a vehicle by uptime, payload, and running cost.",
        hero=dict(mode="still", img="volty-u-1-side-profile", alt="Volty U-1 side profile"),
    ),

    dict(
        slug="design",
        title="VOLTY U-1 | The Design",
        desc="Every part earns its place. The U-1 was drawn for one job: moving goods all day at the lowest cost per kilometer.",
        crumb="Design",
        h1="Every part <em>earns its place.</em>",
        lead="The U-1 was drawn for one job: moving goods, all day, at the lowest cost per kilometer in this market. Nothing on it is decoration.",
        hero=dict(mode="still", img="volty-u-1-exploded-component-view", alt="Volty U-1 exploded component view"),
    ),

    dict(
        slug="difference",
        title="VOLTY U-1 | Why We Are Different",
        desc="VinFast and Gogoro lock riders into a single battery ecosystem. Volty is agnostic by design, the first cross compatible swap platform in Vietnam.",
        crumb="Difference",
        h1="One bike. <em>Every network.</em>",
        lead="VinFast and Gogoro lock riders into a single battery ecosystem. Volty is agnostic by design, the first cross compatible battery swapping utility bike in Vietnam.",
        hero=dict(mode="still", img="volty-u-1-electric-utility-motorcycle", alt="Volty U-1 electric utility motorcycle"),
    ),

    # -------------------------------------------------------------- vehicle
    dict(
        slug="vehicle",
        title="VOLTY U-1 | The Vehicle",
        desc="One chassis, every job. The Volty U-1 accessory platform: front and rear cargo racks, mid rails, side load decks, and a swappable battery bay.",
        crumb="Vehicle",
        h1="One chassis. <em>Every job.</em>",
        lead="The U-1 is not a bike with accessories bolted on. It is a load platform that happens to have two wheels. Inspect any part of the build.",
        hero=dict(mode="hotspot", img=ACC, alt=ACC_ALT, spots=SPOTS),
    ),

    # ----------------------------------------------------------- technology
    dict(
        slug="technology",
        title="VOLTY U-1 | Technology and Systems",
        desc="Network-agnostic battery swapping. One bay, multiple BaaS networks, under two minutes per swap. No vendor lock-in.",
        crumb="Technology",
        h1="Energy without <em>boundaries.</em>",
        lead="VinFast and Gogoro lock a rider into one battery ecosystem. The U-1 bay is engineered for several. Run a swap and pick a network.",
        hero=dict(
            mode="swap",
            nets=[
                dict(name="Dual pack", desc="Two packs, heavy long distance logistics", status="140 to 160 km", packs=2),
                dict(name="Single pack", desc="One pack, nimble urban ride hailing", status="Lower weight", packs=1),
                dict(name="Partner network", desc="Public swap cabinets at partner locations", status="MOU signed", packs=2),
            ],
        ),
    ),

    # ------------------------------------------------------------- audience
    dict(
        slug="audience",
        title="VOLTY U-1 | Who We Build For",
        desc="From food delivery to long-haul logistics. One platform across every major fleet in Vietnam, configured by accessory.",
        crumb="Audience",
        h1="One platform. <em>Every fleet.</em>",
        lead="Ride hailing, food delivery, last mile parcels, corporate logistics. Same chassis, different rig. Pick a segment and watch the build change.",
        hero=dict(
            mode="segments",
            img=ACC, alt=ACC_ALT,
            rig=SPOTS,
            segments=[
                dict(
                    name="Ride Hailing",
                    rig=[4, 5],
                    stats=[
                        dict(k="Daily distance",   v=150, u=" km"),
                        dict(k="Payload used",     v=90,  u=" kg"),
                        dict(k="Battery packs",    v=1,   u=""),
                        dict(k="Rider take home lift", v=38, u="%", hot=True),
                    ],
                    note="Grab and Be riders run long hours on light loads. <b>Single pack, stripped rig, lowest weight.</b> The economics come from the flat swap subscription replacing a pump price that moves every week.",
                ),
                dict(
                    name="Food Delivery",
                    rig=[0, 4, 5],
                    stats=[
                        dict(k="Daily distance",   v=200, u=" km"),
                        dict(k="Payload used",     v=120, u=" kg"),
                        dict(k="Battery packs",    v=2,   u=""),
                        dict(k="Rider take home lift", v=38, u="%", hot=True),
                    ],
                    note="GrabFood and ShopeeFood live on the front rack. <b>Insulated bags over the steering axis, dual pack for the lunch and dinner peaks.</b> Under 2 minute swaps mean no fuel stop inside a delivery window.",
                ),
                dict(
                    name="Last Mile Parcels",
                    rig=[0, 1, 2, 4, 5],
                    stats=[
                        dict(k="Daily distance",   v=200, u=" km"),
                        dict(k="Payload used",     v=170, u=" kg"),
                        dict(k="Battery packs",    v=2,   u=""),
                        dict(k="Saving per unit, yr", v=36.5, u="M ₫", hot=True),
                    ],
                    note="Ahamove and SPX stack boxes. <b>Front rack, mid rails and rear basket, all three.</b> This is the configuration the 200 kg payload rating exists for, and where the TCO gap against petrol is widest.",
                ),
                dict(
                    name="Corporate Logistics",
                    rig=[0, 1, 2, 3, 4, 5],
                    stats=[
                        dict(k="Daily distance",   v=200, u=" km"),
                        dict(k="Payload used",     v=200, u=" kg"),
                        dict(k="Battery packs",    v=2,   u=""),
                        dict(k="Saving per unit, 3 yr", v=109.5, u="M ₫", hot=True),
                    ],
                    note="Viettel Post, GHN and GHTK move freight, not parcels. <b>Full rig including side load decks</b>, for cargo a scooter physically cannot take. At 1,000 units this is roughly 1.4M USD a year in structural cost advantage.",
                ),
            ],
        ),
    ),

    dict(
        slug="contact",
        title="VOLTY U-1 | Contact",
        desc="Fleet pilots, partnerships and rider support. NUEN MOTO Company Limited, Thu Duc City, Ho Chi Minh City.",
        crumb="Contact",
        h1="Let's build the <em>fleet.</em>",
        lead="10 to 100 units, your routes, your riders, real operating data before any fleet commitment.",
        hero=dict(mode="still", img=None, alt=""),
    ),
]
