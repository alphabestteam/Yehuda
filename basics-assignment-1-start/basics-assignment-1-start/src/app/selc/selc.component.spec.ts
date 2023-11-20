import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelcComponent } from './selc.component';

describe('SelcComponent', () => {
  let component: SelcComponent;
  let fixture: ComponentFixture<SelcComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SelcComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SelcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
