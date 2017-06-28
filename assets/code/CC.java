© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

// SAMPLE CODE (Parser)

package com.google.culturalcompass;

import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;
import com.google.culturalcompass.shared.Place;

public class Reader {
	private URL url;
	private InputStream inputStream;
	private Workbook workbook;
	private Sheet sheet;
	private ArrayList<Place> placesToStore;

	public Reader() {
		placesToStore = new ArrayList<Place>();
		try {
			url = new URL(
					"http://www.ugrad.cs.ubc.ca/~n1y8/2015CulturalSpaces.xls");
			inputStream = url.openStream();
			workbook = WorkbookFactory.create(inputStream);
			sheet = workbook.getSheetAt(0);
			sheet.removeRow(sheet.getRow(0));
		} catch (Throwable e) {
			e.printStackTrace();
		}
	}

	public ArrayList<Place> importData() {
		for (Row row : sheet) {
			String dataKey = "";
			String CULTURAL_SPACE_NAME = "";
			String WEBSITE = "";
			String ADDRESS = "";
			double LONGITUDE = 0;
			double LATITUDE = 0;
			for (int i = 0; i < 6; i++) {
				Cell cell = row.getCell(i, Row.RETURN_BLANK_AS_NULL);
				if (i == 0 && cell != null)
					dataKey = cell.getRichStringCellValue().getString();
				else if (i == 1 && cell != null)
					CULTURAL_SPACE_NAME = cell.getRichStringCellValue()
							.getString();
				else if (i == 2 && cell != null)
					WEBSITE = cell.getRichStringCellValue().getString();
				else if (i == 3 && cell != null)
					ADDRESS = cell.getRichStringCellValue().getString();
				else if (i == 4 && cell != null)
					LONGITUDE = cell.getNumericCellValue();
				else if (i == 5 && cell != null)
					LATITUDE = cell.getNumericCellValue();
			}
			// Update Section A
			 if (row.getCell(0).getRichStringCellValue().getString()
			 .contains("A")) {
			 Place place = new Place(dataKey, CULTURAL_SPACE_NAME, WEBSITE,
			 ADDRESS, LATITUDE, LONGITUDE);
			 placesToStore.add(place);
			 }
			// Update section B
			 if (row.getCell(0).getRichStringCellValue().getString()
			 .contains("B")) {
			 Place place = new Place(dataKey, CULTURAL_SPACE_NAME, WEBSITE,
			 ADDRESS, LATITUDE, LONGITUDE);
			 placesToStore.add(place);
			 }
			// Update section C
			 if (row.getCell(0).getRichStringCellValue().getString()
			 .contains("C")) {
			 Place place = new Place(dataKey, CULTURAL_SPACE_NAME, WEBSITE,
			 ADDRESS, LATITUDE, LONGITUDE);
			 placesToStore.add(place);
			 }
			// Update section D
			 if (row.getCell(0).getRichStringCellValue().getString()
			 .contains("D")) {
			 Place place = new Place(dataKey, CULTURAL_SPACE_NAME, WEBSITE,
			 ADDRESS, LATITUDE, LONGITUDE);
			 placesToStore.add(place);
			 }
			// Update section E
			 if (row.getCell(0).getRichStringCellValue().getString()
			 .contains("E")) {
			 Place place = new Place(dataKey, CULTURAL_SPACE_NAME, WEBSITE,
			 ADDRESS, LATITUDE, LONGITUDE);
			 placesToStore.add(place);
			 }
			// Update section F
			 if (row.getCell(0).getRichStringCellValue().getString()
			 .contains("F")) {
			 Place place = new Place(dataKey, CULTURAL_SPACE_NAME, WEBSITE,
			 ADDRESS, LATITUDE, LONGITUDE);
			 placesToStore.add(place);
			 }
		}
		return placesToStore;
	}
}

//------------------------------------------------------------------------------------------------------------------

// SAMPLE CODE (Junit tests)

package com.google.culturalcompass;

import static org.junit.Assert.*;
import java.util.ArrayList;
import org.junit.Before;
import org.junit.Test;
import com.google.culturalcompass.shared.Place;

public class Tester {

	private ArrayList<Place> places;

	@Before
	public void init() throws Exception {
		Reader r = new Reader();
		places = r.importData();
	}

	@Test
	public void testExistingObject() {
		assert (places.contains(new Place("D143", "Railtown Studios",
				"http://railtownstudios.com/",
				"321 Railway St, Vancouver, BC, V6A 1A4", 49.2846363,
				-123.097645)));
	}

	@Test
	public void testNonExistingObject() {
		assert (!places.contains(new Place("A599", "abcdefg", "www.abc.com",
				"1234 abc street", 49.2344352, -123.134319)));
	}

	@Test
	public void testFirstObject() {
		Place place = places.get(0);
		assertEquals(place.getName(),
				"15th Field Artillery Regiment Museum and Archives");
		assertEquals(place.getWebsite(),
				"www.memorybc.ca/museum-of-15th-field-artillery-regiment");
		assertEquals(place.getAddress(),
				("2025 W 11th Av, Vancouver, BC, V6J 2C7"));
		assert (place.getLon() == -123.151123);
		assert (place.getLat() == 49.261938);
	}

	@Test
	public void testMidObject() {
		Place place = places.get(8);
		assertEquals(place.getName(), "Alliance Française de Vancouver");
		assertEquals(place.getWebsite(), "http://www.alliancefrancaise.ca/");
		assertEquals(place.getAddress(),
				("6161 Cambie St, Vancouver, BC, V5Z 3B2"));
		assert (place.getLon() == -123.1169818);
		assert (place.getLat() == 49.228879);
	}

	@Test
	public void testLastObject() {
		Place place = places.get(places.size() - 1);
		assertEquals(place.getName(), "Yuk Yuk's Comedy Club");
		assertEquals(place.getWebsite(), "http://www.yukyuks.com");
		assertEquals(place.getAddress(),
				("2837 Cambie St, Vancouver, BC, V5Z 3Y8"));
		assert (place.getLon() == -123.1151069);
		assert (place.getLat() == 49.2600654);