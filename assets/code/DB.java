© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE

public class Passenger {

	DBManager dbm;

	public Passenger() {
		dbm = new DBManager();
	}

	public boolean addMember(String userid, String email, String passportNo) {
		dbm.connect();
		ResultSet rs = dbm
				.fetch("select count(*) from passenger where passportNo = '"
						+ passportNo + "'");
		int count = 0;
		try {
			while (rs.next()) {
				count = rs.getInt(1);
			}
		} catch (SQLException e) {
			System.out.println("PassportNo does not exist.");
			e.printStackTrace();
		}			//JOptionPane.showMessageDialog(null, "PassportNo does not exist.");
		int i = 0;
		if (count != 0) {
			dbm.iud("insert into member values(" + "'" + userid + "'," + "'"
					+ email + "','" + passportNo + "'," + "0" + ")");
			System.out.println("Congratulations, you are now a member.");
			JOptionPane.showMessageDialog(null, "Congratulations, you are now a member.");
		}
		i+=1;
		dbm.disconnect();
		if (i == 1)
			return true;
		else
			return false;
	}

	public boolean deleteAccount(String userid, String email, String passportNo) {
		dbm.connect();
		int i = 0;
		dbm.iud("delete from member where " + "userid ='" + userid + "'"
				+ " and email ='" + email + "'" + " and passportNo ='"
				+ passportNo + "'");
		System.out.println("Your personal account has been deleted.");
		JOptionPane.showMessageDialog(null, "Your personal account has been deleted.");
		i++;
		dbm.disconnect();
		if (i == 1)
			return true;
		else
			return false;
	}

	public boolean changePersonalInformation(String passportNo, String nEmail,
			String nUserid) {
		dbm.connect();
		int i = 0;
		ResultSet rs = dbm
				.fetch("select count(*) from passenger where passportNo ='"
						+ passportNo + "'");
		int count = 0;
		try {
			while (rs.next()) {
				count = rs.getInt(1);
			}
		} catch (SQLException e) {
			System.out.println("Passenger does not exist in the DB.");
			e.printStackTrace();
		}
		if (count == 0) {
			System.out.println("Failed to update your personal information.");
			JOptionPane.showMessageDialog(null, "Passenger does not exist in the DB.");
		} else {
		dbm.iud("update member set email ='" + nEmail + "'"
	           + ", userid" + "='" + nUserid + "'" + " where passportNo ='"
	           + passportNo + "'");
		System.out.println("Your personal account has been updated.");
		JOptionPane.showMessageDialog(null, "Your personal account has been updated.");
		i++;
		}
		dbm.disconnect();
		if (i == 1)
			return true;
		else
			return false;
	}

	public void checkCredentials(String passportNo) {
		dbm.connect();
		ResultSet rs = dbm
				.fetch("select count(*) from passenger where passportNo ="
						+ "'" + passportNo + "'");
		int count = 0;
		try {
			while (rs.next()) {
				count = rs.getInt(1);
			}
		} catch (SQLException e) {
			System.out.println("Failed.");
			e.printStackTrace();
		}
		if (count != 0) {
			ResultSet rs1 = dbm
					.fetch("select count(*) from member where passportNo ="
							+ "'" + passportNo + "'");
			int count1 = 0;
			try {
				while (rs1.next()) {
					count1 = rs1.getInt(1);
				}
			} catch (SQLException e) {
				System.out.println("Passenger does not exist in the DB.");
				e.printStackTrace();
			}JOptionPane.showMessageDialog(null, "Passenger does not exist in the DB.");
			if (count1 != 0) {
				System.out
						.println("An account already exists with this passportNo.");
				JOptionPane.showMessageDialog(null, "An account already exists with this passportNo.");
			} else {
				System.out
						.println("You are eligible to apply for our membership program.");
				JOptionPane.showMessageDialog(null, "You are eligible to apply for our membership program.");
			}
			dbm.disconnect();
		} else {
			System.out.println("Passenger does not exist in the DB.");
			JOptionPane.showMessageDialog(null, "Passenger does not exist in the DB.");
		}
	}

	public int purchaseTicket(String fName, String lName, String seatNo,
			String flightNo, String passportNo) {
		dbm.connect();
		ResultSet rs = dbm
				.fetch("select count(*) from passenger where passportNo = '"
						+ passportNo + "'");
		int checkExist = 0;
		try {
			while (rs.next()) {
				checkExist = rs.getInt(1);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}

		if (checkExist != 1) {
			dbm.iud("insert into passenger values(" + "'" + passportNo + "'"
					+ ", " + "'" + fName + "'" + ", " + "'" + lName + "'" + ")");
		}
		ResultSet rs1 = dbm.fetch("select MAX(tID) from ticket");
		int newtID = -1;
		try {
			while (rs1.next()) {
				newtID = rs1.getInt(1);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		newtID++;
		dbm.iud("insert into ticket values(" + newtID + ", " + "'" + passportNo
				+ "'" + ", " + "'" + flightNo + "'" + ", " + 0 + ")");
		dbm.iud("update seat set available ='FALSE'" + " where seatNo ='"
				+ seatNo + "'");
		dbm.iud("update ticket set price = (select sum(fcost) as total from (select flightNo,fcost from flight where flightNo ='"
				+ flightNo
				+ "' union all select flightNo,scost as fcost from seat where seatNo = '"
				+ seatNo + "')) where tID =" + newtID);
		dbm.disconnect();
		System.out.println(newtID);
		JOptionPane.showMessageDialog(null, newtID);
		return newtID;
	}

	public ArrayList<String> searchByCity(String city) {
		dbm.connect();
		ArrayList<String> aCode = new ArrayList<String>();
		ResultSet rs = dbm
				.fetch("select acode from airport where upper(city) = upper('"
						+ city + "')");
		try {
			while (rs.next()) {
				ResultSetMetaData metadata = rs.getMetaData();
				int numCols = metadata.getColumnCount();

				for (int i = 0; i < numCols; i++) {
					aCode.add(rs.getString(i + 1));
				}
			}
		} catch (SQLException e) {
			System.out
					.println("City either does not exist or does not contain an airport.");
			e.printStackTrace();
		}
		dbm.disconnect();
		return aCode;
	}

	public ArrayList<String> searchByAirline(String airline) {
		dbm.connect();
		ArrayList<String> flightNo = new ArrayList<String>();
		ResultSet rs = dbm
				.fetch("select acode from airport where upper(city) = upper('"
						+ airline + "')");
		try {
			while (rs.next()) {
				ResultSetMetaData metadata = rs.getMetaData();
				int numCols = metadata.getColumnCount();

				for (int i = 0; i < numCols; i++) {
					flightNo.add(rs.getString(i + 1));
				}
			}
		} catch (SQLException e) {
			System.out.println("The airline does not exist.");
			e.printStackTrace();
		}
		dbm.disconnect();
		return flightNo;
	}

	public HashMap<String, Object> searchByFlightNo(String string) {
		dbm.connect();

		HashMap<String, Object> flight = new HashMap<String, Object>();

		ResultSet rs = dbm.fetch("select * from flight where flightNo = '"
				+ string + "'");

		try {
			while (rs.next()) {
				ResultSetMetaData rsmd = rs.getMetaData();
				int numCols = rsmd.getColumnCount();

				ArrayList<String> columns = new ArrayList<String>();
				for (int i = 0; i < numCols; i++) {
					columns.add(rsmd.getColumnName(i + 1));
				}

				for (String colName : columns) {
					Object value = rs.getObject(colName);
					flight.put(colName, value);
				}
			}
		} catch (SQLException e) {
			System.out.println("The flight does not exist.");
			e.printStackTrace();
		}
		dbm.disconnect();
		return flight;
	}

	public ArrayList<HashMap<String, Object>> searchByAirport(String aCode) {
		dbm.connect();

		ArrayList<HashMap<String, Object>> rows = new ArrayList<HashMap<String, Object>>();

		ResultSet rs = dbm
				.fetch("select * from airport where upper(acode) = upper('"
						+ aCode + "')");

		try {
			while (rs.next()) {
				ResultSetMetaData rsmd = rs.getMetaData();
				int numCols = rsmd.getColumnCount();

				ArrayList<String> columns = new ArrayList<String>();
				for (int i = 0; i < numCols; i++) {
					columns.add(rsmd.getColumnName(i + 1));
				}

				HashMap<String, Object> row = new HashMap<String, Object>();
				for (String colName : columns) {
					Object value = rs.getObject(colName);
					row.put(colName, value);
				}
				rows.add(row);
			}
		} catch (SQLException e) {
			System.out.println("The airport does not exist.");
			e.printStackTrace();
		}
		dbm.disconnect();
		return rows;
	}