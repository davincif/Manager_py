# Game Design Document

## Index

1. [Target Audience](#Target-Audience)
1. [Inspirations](#Inspirations)
1. [Short Description](#Short-Description)
1. [Theme](#Theme)
    1. [Cultural Reference](#Cultural-Reference)
    1. [Look and feel](#Look-and-feel)
1. [Mechanics](#Mechanics)
    1. [Map](#Map)
    1. [Terrains](#Terrains)
    1. [Time](#Time)
    1. [Raw Material](#Raw-Material)
    1. [Resource Tier](#Resource-Tier)
    1. [Structures](#Structures)
1. [Non Functional Requerements](#Non-Functional-Requerements)

## Target Audience

<a name="Target-Audience"></a>

Poeple that where **fans of the RTS and Tycoon games**, browser managers. An audience that takes fun into **strategy**, optimizing **processes** and **exploring**.

Probably **adults** into their **late 20's and beyoung** that grew with **references** like **SimCity and Age of Empires**.

## Inspirations

<a name="Inspirations"></a>

The games takes inspiration into a list of games that, in some degree or another, already made this **mix** between **exploration**, **commerce** and **war**.

For exemple:

-   City builders, like:
    -   [SimCity IV](https://store.steampowered.com/app/24780/SimCity_4_Deluxe_Edition/)
    -   [Cities SkyLines](https://store.steampowered.com/app/255710/Cities_Skylines/).
-   Games where the focus was on the industries, like:
    -   [Simutrans](https://store.steampowered.com/app/434520/Simutrans/)
    -   [Rise of Industries](https://store.steampowered.com/app/671440/Rise_of_Industry/)
-   Some more ballances between the City Builds and the RTS gener, like:
    -   [Pharaoh](https://store.steampowered.com/app/564530/Pharaoh__Cleopatra/)
    -   [Black and White II](https://en.wikipedia.org/wiki/Black_%26_White_2)
-   The classics RTS games, like:
    -   [Age of Empires II](https://store.steampowered.com/app/221380/Age_of_Empires_II_Retired/)
    -   [Age of Mythology](https://store.steampowered.com/app/266840/Age_of_Mythology_Extended_Edition/)
-   The old RTS games like:
    -   [Travian](https://store.steampowered.com/app/266840/Age_of_Mythology_Extended_Edition/)
    -   [Tribal Wars](https://www.tribalwars.com.pt)

## Short Description

<a name="Short-Description"></a>

The attractiveness of this game should come from a of simple concept:

**The power dynamic of the real world!**

It's hard and unfair, but not everything is about war and, was every player peacefully, so would be the game.

1. One is unlikely to survive alone.
1. Economy is the most important part, it's delicated and intrincated.
1. An Army is only needed if you need to protect yourself; or if you want to conquer others.
1. Armies are an expensive asset to build and maintain.

## Theme

<a name="Theme"></a>

What's the teme of the game? The ambience, how it should look.

### Cultural Reference

<a name="Cultural-Reference"></a>

The game is set in **early madieval** era, where **powender was yet not used as weapon**. But **war ships** and long distance **navigations** where already possible.

### Look and feel

<a name="Look-and-feel"></a>

The game is **text based**.

Ech tile in te map, item, or information of any sort is represented by a combination of caracter(s) and color(s).

Each section, whenever needed, will inform the character/color code of each item.

## Mechanics

<a name="Mechanics"></a>

This section will explain, in detail, each and every one of the mechanics that the game should support.

### Map

<a name="Map"></a>

On a global scale, the **world map** is a squared title set. Where the player can see the bioms, cities and any other player contructed mega structure in it.

| **Bioms**         | Crossing Effort |
| ----------------- | --------------- |
| Plain green lands | 100%            |
| Water             | ❌              |
| Forest            | 115%            |
| Mountains         | 200%            |

The player must be able to diferenciate both the biom and the human constructed mega structure in it.

### Terrains

<a name="Terrains"></a>

Inside each title in the world map there is an also squared **local map**.

Here is where the player can place the human structures avilable in the game, like a woodcutter, a foundry or a wall, for exemple.

It's also at this level that the player can actually see the resources available for exploration. Each one of them comes with a randomized ammount of resources per title.

A player cannot place structure on certain terrains.

| **Bioms**         | constructable | Symbol                                                |
| ----------------- | ------------- | ----------------------------------------------------- |
| Plain green lands | ✔️            | <section style="color: #78be2c">"~"</section> or 🌱   |
| Water             | ❌            | <section style="color: #00a6ed">(~)</section> or 🌊   |
| Forest            | ✔️            | <section style="color: #3e811b">/\|\\</section> or 🌲 |
| Mountains         | ❌            | <section style="color: #2f1b3c">/\\</section> or 🗻   |

**Note**: The placing rule above is a general rule that and will be breaked when specified.

### Time

<a name="Time"></a>

The ration of days:second in the game is of **1d:3s**.

That is to say: _1 day in the game takes excatly 3seconds of gameplay_.

This give roughly _18 min for 1 year_.

### Raw Material

<a name="Raw-Material"></a>

The raw materials, a.k.a [teir 0 materials](#Resource-Tier), are the base resources.

Only raw matherials can be extracted directly from the local [terrains](#Terrains).

Each resource tile comes with an average amount of materials, varying in a range of ±2%.

They are:

| **Material** | Symbol                                              | ≈Material/Tile |
| ------------ | --------------------------------------------------- | -------------- |
| Water        | <section style="color: #00a6ed">(~)</section> or 💧 | ∞              |
| Food         | <section style="color: #d79a57">(o)</section> or 🥔 | 1T             |
| Wood         | <section style="color: #623f30">[=]</section> or 🪵 | 10T            |
| Clay         | <section style="color: #ae5626">[@]</section>       | 10T            |
| Stone        | <section style="color: #595959">[•]</section> or 🪨 | 100T           |

**Note**: All be above mesurements are in SI (International System of Units).

### Resource Tier

<a name="Resource-Tier"></a>

[TO BE DEFINED]

### Structures

<a name="Structures"></a>

[TO BE DEFINED]

## Non Functional Requerements

<a name="Non-Functional-Requerements"></a>

The **core logic** of the game, must be as **decoupled** as possible **from** how the game implements its rendering, input treating and everything else that can be call "**engine**".

So as said before, we must be able to change the game **from** a **text based** game to a **to** a **2d game**, using _pygame_ for eg., without having to rewriting all the game logic.

Same goes for multithreading processing.

And even, for the title set system as much as possible. We might wanna use a hexagonal system at some point in the future.

<!-- ## Population

<a name="Population"></a>

Population is **the most important** resource!

Each person in the game is called a **Villain**; and Each villain consumes -1 Food. -->
