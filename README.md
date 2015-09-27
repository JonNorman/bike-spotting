# bike-spotting
_Where are all the bikes at?_

## Overview
By using the [Santander Cycles API](https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml) we can get the location and status of all docking stations in London. Currently the stream refreshes the data every five minutes. Until access to a more frequently updated stream can be secured, these updates are to be interpolated throughout the five minute window with "bursts" on each station when a bike is docked or locked.

## Features to add
1. Interpolated locking and dockings such that the feed appears more "real time".
2. A pretty "burst" effect on each station when a bike is docked or locked (event determines colour).
3. A basic D3 line graph to show the net bike usage throughout the day
4. A playback feature that will play a sped-up day's worth of locks and docks.