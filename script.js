const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];

let score = 0

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log("SpongBob caught a "+jellyfish+" jellyfish");
    identifyJellyfishAndAddPoints(jellyfish,addPoints)
    console.log("score: "+score);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    species = identifySpecies(jellyfish)
    addPoints(species)
}

// Score keeping callback function
function addPoints(species) {
  
    if (speciesPoints[species] == 2 ||speciesPoints[species]==3||speciesPoints[species]==4) {
        score += speciesPoints[species]
    }
    else{
        score++
    }
    
}

// Helper functions
function identifySpecies(jellyfish) {
    switch (jellyfish) {
        case "pink":
            console.log("Patrick identified a " + jellyfish + " jellyfish!");
            return "pink spotted";
        case "blue":
            console.log("Patrick identified a " + jellyfish + " jellyfish!");
            return "blue stinger";
        case "green":
            console.log("Patrick identified a " + jellyfish + " jellyfish!");
            return "green itches";
        default:
            console.log("Patrick identified a common jellyfish!");
            return 9999;
    }
}

//The Adventure Starts Here! 

for (const i in jellyfishDays) {
    score =0
    console.log("lest go Jellyfishing!");
    for(const j in jellyfishDays[i]) {
        catchJellyfish(jellyfishDays[i][j].color,identifyJellyfishAndAddPoints);
    }
    console.log("Great job SpongeBob and Patrick!");
    console.log("final score : " + score);
  }