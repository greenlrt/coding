//package com.mime.minefront.graphics;

import java.util.Random;

public class Screen extends Render {

	private Render test;
	private Render3D render;

	public Screen(int width, int height) {
		super(width, height);
		Random random = new Random();
		render = new Render3D(width, height);
		test = new Render(256, 256);
		for (int i = 0; i < 256*256; i++) {
			test.pixels[i] = random.nextInt();
		}

	}

	public void render(Game game) {
		for (int i = 0; i < width * height; i++) {
			pixels[i] = 0;
		}
		
		for (int i = 0; i < 50; i++) {
			int anim = (int) (Math.sin(game.time  + i) % 1000);
			int anim2 = (int) (Math.cos(game.time + i) % 1000);
		//	draw(test, (width - 256) / 2 + anim, (height - 256) / 2 + anim2);
		}

		render.floor();
		draw (render, 0, 0);
	}

}
