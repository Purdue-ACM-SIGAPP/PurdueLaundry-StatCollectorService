DROP TABLE Machine;
CREATE TABLE Machine (
  Name varchar NOT NULL,
  Dorm varchar NOT NULL,
  PRIMARY KEY (Name, Dorm)
);

DROP TABLE MachineStateLog;
CREATE TABLE MachineStateLog (
  MachineName varchar NOT NULL,
  MachineDorm varchar NOT NULL,
  StartTime DATE,
  State varchar NOT NULL,
  TimeLeft NUMERIC DEFAULT 0, 
  FOREIGN KEY (MachineName, MachineDorm) REFERENCES Machine(Name, Dorm),
  PRIMARY KEY (MachineName, MachineDorm, StartTime)
);