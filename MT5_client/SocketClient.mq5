//+-----------------------------------------------------------------+
//|                                                     License: MIT |
//|                                      https://github.com/hafezmehr|
//+------------------------------------------------------------------+
#property link      "https://github.com/hafezmehr"
#property version   "1.00"

#include  <ExchangeData.mqh>


//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//---
   int socket=SocketCreate();
   if(socket!=INVALID_HANDLE)
   {
      bool sockcon = SocketConnect(socket,"192.168.1.15",14201,1000);
      if(sockcon == true)
      {
         Print("Connected to "," 192.168.1.15",":",14201);
         double oppr[];
         int copyedo = CopyOpen(_Symbol,_Period,0,lrlenght,oppr);
         double hipr[];
         int copyedh = CopyHigh(_Symbol,_Period,0,lrlenght,hipr);
         double lopr[];
         int copyedl = CopyLow(_Symbol,_Period,0,lrlenght,lopr);
         double clpr[];
         int copyedc = CopyClose(_Symbol,_Period,0,lrlenght,clpr);
         
         string tosend;
         for(int i=0;i<ArraySize(clpr);i++)
         {
            tosend+=(string)oppr[i]+",";
            tosend+=(string)hipr[i]+",";
            tosend+=(string)lopr[i]+",";
            tosend+=(string)clpr[i]+" "; 
         }
         
         bool senddata = socksend(socket, tosend);
         string recieveddata = socketreceive(socket, 1000);
         Print(recieveddata);
         SocketClose(socket);
       
      }
      else
      {
          Print("Connection ","192.168.1.15",":",14201," error ",GetLastError());
          SocketClose(socket);
      }
  
   }
   else
   {
      Print("Socket creation error ",GetLastError());
   }
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//---
   
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
   int socket=SocketCreate();
   if(socket!=INVALID_HANDLE)
   {
      bool sockcon = SocketConnect(socket,"192.168.1.15",14201,1000);
      if(sockcon == true)
      {
         Print("Connected to "," 192.168.1.15",":",14201);
         double oppr[];
         int copyedo = CopyOpen(_Symbol,_Period,0,lrlenght,oppr);
         double hipr[];
         int copyedh = CopyHigh(_Symbol,_Period,0,lrlenght,hipr);
         double lopr[];
         int copyedl = CopyLow(_Symbol,_Period,0,lrlenght,lopr);
         double clpr[];
         int copyedc = CopyClose(_Symbol,_Period,0,lrlenght,clpr);
         
         string tosend;
         for(int i=0;i<ArraySize(clpr);i++)
         {
            tosend+=(string)oppr[i]+",";
            tosend+=(string)hipr[i]+",";
            tosend+=(string)lopr[i]+",";
            tosend+=(string)clpr[i]+" "; 
         }
         
         bool senddata = socksend(socket, tosend);
         string recieveddata = socketreceive(socket, 1000);
         Print(recieveddata);
         SocketClose(socket);
       
      }
      else
      {
          Print("Connection ","192.168.1.15",":",14201," error ",GetLastError());
          SocketClose(socket);
      }
  
   }
   else
   {
      Print("Socket creation error ",GetLastError());
   }
  
   
  }
