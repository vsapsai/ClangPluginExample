//
//  DetailViewController.h
//  SampleProject
//
//  Created by Volodymyr Sapsai on 12/7/13.
//  Copyright (c) 2013 Volodymyr Sapsai. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController

@property (strong, nonatomic) id detailItem;

@property (weak, nonatomic) IBOutlet UILabel *detailDescriptionLabel;
@end
