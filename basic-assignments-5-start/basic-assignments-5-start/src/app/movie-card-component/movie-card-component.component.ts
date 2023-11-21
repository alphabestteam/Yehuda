import { Component } from '@angular/core';
import { FILMS } from '../star-wars-fake-db/film-data';

@Component({
  selector: 'app-movie-card-component',
  templateUrl: './movie-card-component.component.html',
  styleUrls: ['./movie-card-component.component.scss'],
})
export class MovieCardComponentComponent {
  movies = FILMS;
  
  title = 'basics-assignments-5-start';
  opening_crawl = `Luke Skywalker has returned to
    his home planet of Tatooine in
    an attempt to rescue his
    friend Han Solo from the
    clutches of the vile gangster
    Jabba the Hutt.
    
    Little does Luke know that the
    GALACTIC EMPIRE has secretly
    begun construction on a new
    armored space station even
    more powerful than the first
    dreaded Death Star.
    
    When completed, this ultimate
    weapon will spell certain doom
    for the small band of rebels
    struggling to restore freedom
    to the galaxy...`;
}
