import random

o_adjectives = [
    "Vast",
    "Deep",
    "Endless",
    "Turbulent",
    "Serene",
    "Majestic",
    "Rippling",
    "Choppy",
    "Calm",
    "Crystal-clear",
    "Mysterious",
    "Boundless",
    "Tempestuous",
    "Roaring",
    "Mesmerizing",
    "Glistening",
    "Sparkling",
    "Expansive",
    "Ethereal",
    "Breathtaking",
    "Moonlit",
    "Sunlit",
    "Shimmering",
    "Salty",
    "Harmonious",
    "Sapphire",
    "Azure",
    "Teeming",
    "Inviting",
    "Untamed",
    "Raging",
    "Tranquil",
    "Peaceful",
    "Timeless",
    "Infinite",
    "Luminous",
    "Radiant",
    "Pristine",
    "Unspoiled",
    "Murmuring",
    "Tumultuous",
    "Reflective",
    "Lonely",
    "Secluded",
    "Windswept",
    "Dazzling",
    "Picturesque",
    "Abyssal",
    "Ageless",
    "Nautical",
    "Immeasurable",
    "Silent",
    "Alluring",
    "Idyllic",
    "Daunting",
    "Vibrant",
    "Sweeping",
    "Iridescent",
    "Beckoning",
    "Spectacular",
    "Epic",
    "Boundless",
    "Tidal",
    "Surging",
    "Majestic",
    "Grand",
    "Limitless",
    "Uncharted",
    "Bubbling",
    "Dense",
    "Unfathomable",
    "Soothing"
]

p_adjectives = [
    "Lush",
    "Verdant",
    "Rocky",
    "Rolling",
    "Barren",
    "Expansive",
    "Golden",
    "Fertile",
    "Windswept",
    "Undulating",
    "Wild",
    "Rugged",
    "Flat",
    "Vast",
    "Grassy",
    "Arid",
    "Flowering",
    "Serene",
    "Endless",
    "Green",
    "Sunlit",
    "Moonlit",
    "Peaceful",
    "Dry",
    "Fresh",
    "Gentle",
    "Parched",
    "Remote",
    "Sparse",
    "Rich",
    "Unspoiled",
    "Mesmeric",
    "Picturesque",
    "Natural",
    "Open",
    "Sprawling",
    "Idyllic",
    "Bright",
    "Shimmering",
    "Secluded",
    "Bountiful",
    "Stony",
    "Sandy",
    "Pristine",
    "Rippling",
    "Distant",
    "Sparse",
    "Elevated",
    "Tranquil",
    "Timeless",
    "Boundless",
    "Glistening",
    "Inviting",
    "Majestic",
    "Unending",
    "Panoramic",
    "Silent",
    "Lonely",
    "Harmonious",
    "Sparse",
    "Pleasant",
    "Vibrant",
    "Ancient",
    "Uncharted",
    "Breezy",
    "Calm",
    "Mystical",
    "Radiant",
    "Uninhabited"
]

h_adjectives = [
    "Rolling",
    "Gentle",
    "Steep",
    "Rugged",
    "Lush",
    "Verdant",
    "Barren",
    "Rocky",
    "Undulating",
    "Majestic",
    "High",
    "Low",
    "Breathtaking",
    "Serene",
    "Slopey",
    "Grassy",
    "Leafy",
    "Tree-covered",
    "Bare",
    "Mossy",
    "Picturesque",
    "Panoramic",
    "Elevated",
    "Humped",
    "Rising",
    "Towering",
    "Lonely",
    "Solitary",
    "Remote",
    "Isolated",
    "Fertile",
    "Rich",
    "Craggy",
    "Stony",
    "Green",
    "Flourishing",
    "Dense",
    "Sparse",
    "Pleasant",
    "Tranquil",
    "Harsh",
    "Sunny",
    "Shaded",
    "Dappled",
    "Golden",
    "Sunlit",
    "Misty",
    "Foggy",
    "Hazy",
    "Silhouetted",
    "Dewy",
    "Windswept",
    "Whistling",
    "Echoing",
    "Resplendent",
    "Looming",
    "Dominant",
    "Imposing",
    "Receding",
    "Ancient",
    "Weathered",
    "Eroded",
    "Cultivated",
    "Wild",
    "Unspoiled",
    "Jagged",
    "Serrated",
    "Tiered",
    "Layered",
    "Serrated",
    "Secluded",
    "Vibrant",
    "Idyllic",
    "Inviting",
    "Alluring"
]

m_adjectives = [
    "Majestic",
    "Lofty",
    "Elevated",
    "Sky-high",
    "Snow-capped",
    "Rugged",
    "Jagged",
    "Rocky",
    "Serrated",
    "Towering",
    "Steep",
    "Impressive",
    "Formidable",
    "Grand",
    "Gigantic",
    "Imposing",
    "Magnificent",
    "Vast",
    "Expansive",
    "Massive",
    "Mighty",
    "Dominant",
    "Breathtaking",
    "Splendid",
    "Daunting",
    "Barren",
    "Sparse",
    "Dense",
    "Verdant",
    "Lush",
    "Green",
    "Snowy",
    "Glacial",
    "Frozen",
    "Volcanic",
    "Stony",
    "Granite",
    "Limestone",
    "Basaltic",
    "Silvery",
    "Gleaming",
    "Radiant",
    "Sun-kissed",
    "Shadowy",
    "Misty",
    "Foggy",
    "Cloud-covered",
    "Windswept",
    "Isolated",
    "Remote",
    "Ancient",
    "Timeless",
    "Primordial",
    "Sacred",
    "Spiritual",
    "Mysterious",
    "Enchanting",
    "Foreboding",
    "Harsh",
    "Wild",
    "Rough",
    "Untamed",
    "Unyielding",
    "Inaccessible",
    "Dramatic",
    "Pristine",
    "Secluded",
    "Solitary",
    "Craggy",
    "Desolate",
    "Climbable",
    "Unreachable",
    "Peaked",
    "Rounded",
    "Plateaued",
    "Gentle",
    "Rolling",
    "Resilient",
    "Immutable",
    "Enduring",
    "Eternal",
    "Spectacular",
    "Picturesque",
    "Idyllic"
]

f_adjectives = [
   "Dense",
    "Lush",
    "Verdant",
    "Leafy",
    "Shady",
    "Thick",
    "Overgrown",
    "Wild",
    "Untamed",
    "Majestic",
    "Tranquil",
    "Serene",
    "Peaceful",
    "Silent",
    "Noisy",
    "Vibrant",
    "Bustling",
    "Alive",
    "Teeming",
    "Enchanted",
    "Mystical",
    "Ancient",
    "Ageless",
    "Primeval",
    "Sacred",
    "Spiritual",
    "Mossy",
    "Damp",
    "Wet",
    "Dry",
    "Deciduous",
    "Coniferous",
    "Tropical",
    "Temperate",
    "Evergreen",
    "Broadleaf",
    "Dark",
    "Gloomy",
    "Sunny",
    "Bright",
    "Canopied",
    "Shadowy",
    "Twinkling",
    "Murmuring",
    "Rustling",
    "Whispering",
    "Breezy",
    "Windless",
    "Scented",
    "Fragrant",
    "Pungent",
    "Stagnant",
    "Cool",
    "Crisp",
    "Muggy",
    "Humid",
    "Secluded",
    "Remote",
    "Isolated",
    "Hidden",
    "Virgin",
    "Untouched",
    "Endless",
    "Expansive",
    "Boundless",
    "Pristine",
    "Gnarled",
    "Twisted",
    "Towering",
    "Lofty",
    "Stalwart",
    "Unyielding",
    "Imposing",
    "Impenetrable",
    "Sparse",
    "Rugged",
    "Rough",
    "Jungly",
    "Thorny",
    "Brushy",
    "Vast",
    "Enveloping",
    "Mysterious",
    "Eerie",
    "Foreboding",
    "Idyllic",
    "Picturesque",
    "Dreamy",
    "Inviting",
    "Unsettling",
    "Menacing"
]
#######################
o_nouns = [
    "Abyss",
    "Atoll",
    "Basin",
    "Bay",
    "Bight",
    "Billow",
    "Channel",
    "Chasm",
    "Cove",
    "Current",
    "Deep",
    "Delta",
    "Depression",
    "Drop-off",
    "Edifice",
    "Estuary",
    "Expanse",
    "Fathom",
    "Fjord",
    "Flats",
    "Gulf",
    "Harbor",
    "Haven",
    "Inlet",
    "Isle",
    "Jetty",
    "Kelp Forest",
    "Lagoon",
    "Maelstrom",
    "Main",
    "Mangrove",
    "Marina",
    "Narrows",
    "Ocean",
    "Passage",
    "Pinnacle",
    "Plateau",
    "Reef",
    "Ridge",
    "Rift",
    "Rise",
    "Sandbank",
    "Seabed",
    "Seamount",
    "Shoal",
    "Shore",
    "Sound",
    "Spring",
    "Strait",
    "Surf",
    "Swirl",
    "Tidal Pool",
    "Tide",
    "Trench",
    "Trough",
    "Undercurrent",
    "Upwelling",
    "Vortex",
    "Wave",
    "Whirlpool"
]

p_nouns = [
  "Acres",
    "Barrow",
    "Bluff",
    "Brae",  # a hillside especially along a river
    "Breadth",
    "Clearing",
    "Dale",
    "Dell",
    "Downs",
    "Expanse",
    "Field",
    "Flats",
    "Grassland",
    "Grove",
    "Heath",
    "Hollow",
    "Horizon",
    "Knoll",
    "Land",
    "Lea",  # a meadow or grassy area
    "Meadow",
    "Moor",
    "Orchard",
    "Pampas",
    "Pasture",
    "Prairie",
    "Range",
    "Ridge",
    "Rise",
    "Savannah",
    "Steppe",
    "Stretch",
    "Sward",  # a portion of ground covered with grass
    "Terrace",
    "Thicket",
    "Tundra",
    "Valley",
    "Vale",
    "Vista",
    "Wold",  # a piece of high, open land
    "Yard"
]

h_nouns = [
    "Ascent",
    "Bank",
    "Brae",
    "Climb",
    "Crest",
    "Dale",
    "Decline",
    "Dell",
    "Descent",
    "Dune",
    "Elevation",
    "Embankment",
    "Escarpment",
    "Foothill",
    "Heights",
    "Highland",
    "Hillock",
    "Incline",
    "Knoll",
    "Mound",
    "Peak",
    "Pinnacle",
    "Plateau",
    "Ridge",
    "Rise",
    "Roll",
    "Slope",
    "Summit",
    "Terrace",
    "Tumulus",
    "Upland"
]

m_nouns = [
    "Apex",
    "Base",
    "Bluff",
    "Butte",
    "Canyon",
    "Cirque",
    "Cliff",
    "Crag",
    "Divide",
    "Face",
    "Flank",
    "Gorge",
    "Massif",
    "Pass",
    "Peak",
    "Pinnacle",
    "Ravine",
    "Ridge",
    "Saddle",
    "Sierra",
    "Spire",
    "Summit",
    "Tor",
    "Trench",
    "Valley",
    "Vista",
    "Volcano",
    "Notch",
    "Gully",
    "Col",
    "Bowl",
    "Arête"
]

f_nouns = [
    "Canopy",
    "Clearing",
    "Copse",
    "Dell",
    "Den",
    "Fern",
    "Glade",
    "Grove",
    "Hollow",
    "Meadow",
    "Path",
    "Pond",
    "Ravine",
    "River",
    "Stream",
    "Thicket",
    "Tree",
    "Underbrush",
    "Vale",
    "Waterfall",
    "Woodland",
    "Trail",
    "Creek",
    "Log",
    "Stump",
    "Brook",
    "Brush",
    "Bramble",
    "Clearing",
]

t_name = [
     "Seabreeze Harbor",
    "Coral Cove",
    "Pirate's Cove",
    "Mermaid's Lagoon",
    "Skull Island",
    "Siren's Song",
    "Shipwreck Bay",
    "Treasure Isle",
    "Turtle Beach",
    "Moonlit Bay",
    "Sunset Shores",
    "Whalebone Village",
    "Azure Cove",
    "Mystic Isle",
    "Jungle Landing",
    "Pearl Harbor",
    "Windward Port",
    "Golden Sands",
    "Emerald Cove",
    "Dragonstone Port",
    "Kraken's Keep",
    "Blackbeard Bay",
    "Tidal Haven",
    "Sapphire Isle",
    "Stormy Harbor",
    "Rustic Wharf",
    "Whispering Pines",
    "Moonlit Haven",
    "Silvermoon Bay",
    "Hidden Anchorage",
     "Starfish Cove",
    "Misty Harbor",
    "Crimson Bay",
    "Dolphin's Cove",
    "Emerald Harbor",
    "Tropical Breeze",
    "Marine Village",
    "Cursed Cove",
    "Rainbow Shores",
    "Turtle Island",
    "Pirate's Paradise",
    "Witch's Haven",
    "Crystal Waters",
    "Coral Harbor",
    "Rusty Anchor",
    "Moonlit Oasis",
    "Ghostly Port",
    "Lighthouse Landing",
    "Fisherman's Retreat",
    "Dragon's Den",
    "Sapphire Harbor",
    "Jewel Bay",
    "Golden Sands Cove",
    "Treasure Cove",
    "Seashell Haven",
    "Abyssal Abyss",
    "Mystic Cove",
    "Mango Bay",
    "Silvershore",
    "Stormy Waters",
    "Merfolk's Refuge",
    "Wavesong Harbor",
    "Maritime Village",
    "Sunset Bay",
    "Amber Cove",
    "Kraken's Lair",
    "Tidepool Haven",
    "Whispering Pines Cove",
    "Cursed Island",
    "Blackwater Harbor",
    "Whale Song Bay",
    "Dragon's Breath Port",
    "Pirate's Retreat",
    "Pearl Cove",
    "Coral Reef Port",
    "Moonlit Lagoon",
    "Azure Harbor",
    "Rogue's Retreat",
    "Rainbow Harbor",
    "Hidden Treasure Bay",
    "Siren's Cove",
    "Volcano Bay",
    "Skeleton Island",
    "Crimson Harbor",
    "Witch's Cove",
    "Emerald Oasis",
    "Haunted Harbor",
    "Misty Shores",
    "Crystal Cove",
    "Mystical Waters",
    "Tidal Village",
    "Galleon's Graveyard",
    "Silverstrand Bay",
    "Palm Paradise",
    "Lighthouse Cove",
    "Dragon's Roar Port",
    "Sapphire Shores",
    "Mystic Sands",
    "Jewel Harbor",
    "Golden Anchor Bay",
    "Treasure Hunter's Haven",
    "Seashell Cove",
    "Abyssal Port",
    "Starfish Haven",
    "Sunken Ship Bay",
    "Cursed Treasure Cove",
    "Mermaid's Harbor",
    "Wavesong Village",
    "Coral Beach",
    "Siren's Retreat",
    "Black Pearl Cove",
    "Whale's Tail Bay",
    "Dragon's Claw Port",
    "Turtle Shell Cove",
    "Moonlit Cove",
    "Marine Haven",
    "Ghost Ship Bay",
    "Silvermoon Harbor",
    "Stormy Shore",
    "Turtle Haven",
    "Crystal Cove Village",
    "Mystic Bay",
    "Pirate's Rest",
    "Pearl Harbor Cove",
    "Sunset Oasis",
    "Treasure Trove Bay",
    "Emerald Sound",
    "Crimson Shores",
    "Dolphin Cove",
    "Sapphire Shores Cove",
    "Rusty Cutlass Cove",
    "Pirate's Plunder",
    "Misty Mirage",
    "Crimson Cove",
    "Aqua Bay",
    "Emerald Enclave",
    "Tropical Treasure",
    "Marina Vista",
    "Witch's Wharf",
    "Rainbow Retreat",
    "Atlantis Haven",
    "Dragon's Lair",
    "Sapphire Serenity",
    "Mermaid's Hideaway",
    "Jewel Junction",
    "Golden Galleon",
    "Treasure Trove",
    "Seaweed Sanctuary",
    "Abyssal Abyss",
    "Mystic Mirage",
    "Mango Mist",
    "Silver Serenity",
    "Stormy Secrets",
    "Merfolk's Marina",
    "Whispering Waters",
    "Marine Mysteries",
    "Sunset Serenade",
    "Amber Anchorage",
    "Kraken's Abyss",
    "Tidepool Tavern",
    "Coral Dreams",
    "Rusty Shipyard",
    "Moonlit Magic",
    "Ghost Ship Harbor",
    "Lighthouse Lookout",
    "Fisherman's Fortune",
    "Dragon's Dominion",
    "Sapphire Serenade",
    "Jewel Junction",
    "Golden Grotto",
    "Treasure Trail",
    "Seashell Shores",
    "Abyssal Adventure",
    "Mystic Magic",
    "Mango Mirage",
    "Silvershore Sanctuary",
    "Stormy Splendor",
    "Mermaid's Melody",
    "Wavesong Wharf",
    "Maritime Marvel",
    "Sunset Serenity",
    "Amber Azure",
    "Kraken's Keep",
    "Tidepool Treasure",
    "Coral Cove",
    "Rainbow Reflections",
    "Hidden Harbor",
    "Siren's Serenade",
    "Volcano Vista",
    "Skeleton's Cove",
    "Crimson Cape",
    "Witch's Wonders",
    "Emerald Echoes",
    "Haunted Hideaway",
    "Misty Mysteries",
    "Crystal Cascades",
    "Mystical Mirage",
    "Tidal Treasures",
    "Galleon's Gold",
    "Silverstrand Serenity",
    "Palm Paradise Cove",
    "Lighthouse Lookout",
    "Dragon's Domain",
    "Sapphire Splendor",
    "Mystic Meadows",
    "Jewel Junction Cove",
    "Golden Galleon Bay",
    "Treasure Hunter's Hideaway",
    "Seashell Serenity",
    "Abyssal Atoll",
    "Starfish Sanctuary",
    "Sunken Secrets",
    "Cursed Caverns",
    "Mermaid's Melody",
    "Wavesong Wonders",
    "Coral Cove Cove",
    "Siren's Sanctuary",
    "Black Pearl Bay",
    "Whale's Watch",
    "Dragon's Dominion Cove",
    "Turtle's Treasure",
    "Moonlit Mysteries",
    "Marine Marvel",
    "Ghost Ship Grotto",
    "Silvermoon Serenade",
    "Stormy Splendors",
    "Turtle's Tranquility",
    "Crystal Cove Cove",
    "Mystic Magic Cove",
    "Pirate's Paradise Cove",
    "Pearl Harbor Cove",
    "Sunset Serenity Cove",
    "Treasure Trove Cove",
    "Emerald Echoes Cove",
    "Crimson Cove Cove",
    "Dolphin's Delight Cove",
    "Sapphire Splendor Cove",
    "Rusty Relic Cove",
    "Pirate's Perch",
    "Mystic Mirage Cove",
    "Crimson Shores Cove",
    "Aqua Haven",
    "Emerald Shores Cove",
    "Tropical Tranquility",
    "Marina Vista Cove",
    "Witch's Wharf Cove",
    "Rainbow Reef Cove",
    "Atlantis Oasis",
    "Dragon's Roost",
    "Sapphire Serenity Cove",
    "Mermaid's Cove",
    "Jewel Junction Cove",
    "Golden Grotto Cove",
    "Treasure Cove Cove",
    "Seashell Cove Cove",
    "Abyssal Abyss Cove",
    "Mystic Mirage Cove Cove",
    "Mango Mist Cove",
    "Silver Serenity Cove Cove",
    "Stormy Secrets Cove",
    "Merfolk's Marina Cove",
    "Whispering Waters Cove",
    "Marine Mysteries Cove",
    "Sunset Serenade Cove",
    "Amber Anchorage Cove",
    "Kraken's Abyss Cove",
    "Tidepool Tavern Cove",
    "Coral Dreams Cove",
    "Rusty Shipyard Cove",
    "Moonlit Magic Cove",
    "Ghost Ship Harbor Cove",
    "Lighthouse Lookout Cove",
    "Fisherman's Fortune Cove",
    "Dragon's Roost Cove",
    "Sapphire Serenade Cove Cove",
    "Jewel Junction Cove Cove",
    "Golden Grotto Cove Cove",
    "Treasure Trail Cove",
    "Seashell Shores Cove Cove",
    "Abyssal Adventure Cove",
    "Mystic Magic Cove Cove",
    "Mango Mirage Cove",
    "Silvershore Sanctuary Cove Cove",
    "Stormy Splendor Cove",
    "Mermaid's Melody Cove",
    "Wavesong Wharf Cove Cove",
    "Maritime Marvel Cove",
    "Sunset Serenity Cove Cove",
    "Amber Azure Cove",
    "Kraken's Keep Cove",
    "Tidepool Treasure Cove Cove",
    "Coral Cove Cove Cove",
    "Rainbow Reflections Cove",
    "Hidden Harbor Cove",
    "Siren's Serenade Cove",
    "Volcano Vista Cove",
    "Skeleton's Cove Cove",
    "Crimson Cape Cove",
    "Witch's Wonders Cove",
    "Emerald Echoes Cove",
    "Haunted Hideaway Cove",
    "Misty Mysteries Cove",
    "Crystal Cascades Cove",
    "Mystical Mirage Cove Cove",
    "Tidal Treasures Cove",
    "Galleon's Gold Cove",
    "Silverstrand Serenity Cove Cove",
        "Portsmouth",
    "Harborview",
    "Seaview",
    "Anchor's End",
    "Marinatown",
    "Bayshore",
    "Cresthaven",
    "Lakewood",
    "Fairharbor",
    "Windsor Cove",
    "Stonebridge",
    "Brookside",
    "Kingsport",
    "Newport",
    "Havenfield",
    "Oceanville",
    "Rivertown",
    "Greenwich",
    "Cliffside",
    "Fishingham",
    "Millville",
    "Riverside",
    "Harbor Springs",
    "Highland Bay",
    "Covebridge",
    "Piermont",
    "Hollyville",
    "Shoreside",
    "Maplewood",
    "Harborside",
    "Lighthouse Bay",
    "Rockport",
    "Beachwood",
    "Bayside",
    "Tidewater",
    "Sailor's Cove",
    "Summerfield",
    "Bridgewater",
    "Harborview Cove",
    "Meadowville",
    "Waverly",
    "Fisher's Cove",
    "Havenbrook",
    "Crestwood",
    "Rivershore",
    "Windward Bay",
    "Pinecrest",
    "Newbridge",
    "Seawinds",
    "Bayside Heights",
    "Seabrook",
    "Greenfield",
    "Portside",
    "Lakemont",
    "Marinaville",
    "Harborside Cove",
    "Tidewatch",
    "Shorehaven",
    "Fairwind",
    "Bayfield",
    "Oakridge",
    "Waterside",
    "Riverbend",
    "Sailor's Point",
    "Havenridge",
    "Brookside Cove",
    "Anchor's Landing",
    "Lighthouse Cove",
    "Woodbridge",
    "Riverside Cove",
    "Harborview Heights",
    "Harborside Village",
    "Highland Cove",
    "Crestwood Bay",
    "Bayside Park",
    "Cliffside Cove",
    "Seaside",
    "Seaview Cove",
    "Kingsbridge",
    "Piercove",
    "Lakemeadow",
    "Ocean Bay",
    "Harbor's Edge",
    "Fisher's Landing",
    "Bayside Point",
    "Bayhill",
    "Maplebridge",
    "Port Haven",
    "Waterside Village",
    "Lighthouse Point",
    "Sailor's Haven",
    "Bridgewater Cove",
    "Greenbriar",
    "Seaglen",
    "Marina Bay",
    "Tidewatch Cove",
    "Harbor Heights",
    "Riverbend Cove",
    "Bayside Terrace",
    "Crestwood Village",
    "Harbor's View",
    "Bayview Cove",
    "Brookside Village",
    "Shoreline",
    "Portside Cove",
    "Riverview",
    "Bayside Harbor",
    "Marinavista",
    "Bayfront",
    "Harbor Bayou",
    "Cliffview Cove",
    "Seahaven",
    "Harborwalk",
    "Bridgetown",
    "Lakeside",
    "Oceanwood",
    "Waveridge",
    "Seawind Cove",
    "Crestbrook",
    "Pier Harbor",
    "Harbor Village",
    "Coastal Cove",
    "Woodside",
    "Harbor Isle",
    "Bayside Cove Cove",
    "Baycrest",
    "Marinaville Cove",
    "Beachside",
    "Bridgewood",
    "Tideview",
    "Anchor's Cove",
    "Harborfield",
    "Bayshire",
    "Harborview Village",
    "Seascape Cove",
    "Harbor Cove Cove",
    "Portside Bay",
    "Riverside Village",
    "Bayshore Cove",
    "Marinatown Cove",
    "Cliffview Bay",
        "Seaspray",
    "Piermont Village",
    "Bayview Landing",
    "Havenbridge Cove",
    "Crestwood Harbor",
    "Maritime Point",
    "Beachfront Bay",
    "Harborwatch Cove",
    "Shoreside Village",
    "Seagrove",
    "Seabridge",
    "Anchor's Landing",
    "Fairview Cove",
    "Marinavista Bay",
    "Bayfield Terrace",
    "Lighthouse Pointe",
    "Ocean Crest",
    "Bridgewater Bay",
    "Rivertown Haven",
    "Harborside Bayou",
    "Harbor's Reach",
    "Woodside Haven",
    "Bayside Cove Heights",
    "Harborwalk Village",
    "Harborfield Heights",
    "Portside Bay Park",
    "Riverside Haven Cove",
    "Bayshore Coveview",
    "Marinatown Pointe",
    "Cliffview Bayport",
    "Harborside Vista",
    "Seahaven Shore",
    "Harborwalk Landing",
    "Bridgetown Shoreline",
    "Lakeside Bayview",
    "Oceanwood Bayfront",
    "Waveridge Port",
    "Seawind Harbor Village",
    "Crestbrook Harbor",
    "Pier Harbor Point",
    "Harbor Village Crossing",
    "Coastal Cove Beach",
    "Woodside Bayfront",
    "Harbor Isle Point",
    "Bayside Heights Crossing",
    "Baycrest Bayview",
    "Marinaville Pier",
    "Beachside Baywalk",
    "Bridgewood Shore",
    "Tideview Pointe",
    "Anchor's Reach",
    "Harborfield Baywood",
    "Bayshire Harbor",
    "Harborview Village Point",
    "Seascape Port",
    "Harbor Reach",
    "Portside Bay Harbor",
    "Riverside Village Crossing",
    "Bayshore Harborview",
    "Marinatown Point Landing",
    "Cliffview Bay Landing",
    "Harborside Bay Point",
    "Seahaven Shoreline",
    "Harborwalk Landing Point",
    "Bridgetown Shoreline Crossing",
    "Lakeside Bayview Point",
    "Oceanwood Bayfront Village",
    "Waveridge Port Crossing",
    "Seawind Harbor Village Point",
    "Crestbrook Harbor Point",
    "Pier Harbor Point Landing",
    "Harbor Village Crossing Point",
    "Coastal Cove Beach Landing",
    "Woodside Bayfront Landing",
    "Harbor Isle Point Village",
    "Bayside Heights Crossing Point",
    "Baycrest Bayview Point",
    "Marinaville Pier Village",
    "Beachside Baywalk Landing",
    "Bridgewood Shore Point",
    "Tideview Pointe Landing",
    "Anchor's Reach Village",
    "Harborfield Baywood Landing",
    "Bayshire Harbor Village",
    "Harborview Village Point Landing",
    "Seascape Port Village",
    "Harbor Reach Point",
    "Portside Bay Harbor Landing",
    "Riverside Village Crossing Point",
    "Bayshore Harborview Village",
    "Marinatown Point Landing Village",
    "Cliffview Bay Landing Village",
    "Harborside Bay Point Village",
    "Seahaven Shoreline Village",
]

def random_feature(char):
    if char == "O":
        rng = random.randint(1,10)
        if rng == 10:
            return f"{random.choice(o_adjectives)} {random.choice(o_nouns)}"
    if char == "P":
        return f"{random.choice(p_adjectives)} {random.choice(p_nouns)}"
    if char == "H":
        return f"{random.choice(h_adjectives)} {random.choice(h_nouns)}"
    if char == "M":
        return f"{random.choice(m_adjectives)} {random.choice(m_nouns)}"
    if char == "F":
        return f"{random.choice(f_adjectives)} {random.choice(f_nouns)}"
    if char == "T":
        return f"{random.choice(t_name)}"
    return ""