#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Airtable Manager - Manages connection with Airtable CRM
"""

import os
from datetime import datetime
from pyairtable import Api
import logging

logger = logging.getLogger(__name__)


class AirtableManager:
    def __init__(self):
        """Initialize connection to Airtable"""
        self.api_key = os.getenv('AIRTABLE_API_KEY')
        self.base_id = os.getenv('AIRTABLE_BASE_ID')
        
        if not self.api_key or not self.base_id:
            raise ValueError("Missing AIRTABLE_API_KEY or AIRTABLE_BASE_ID in environment variables")
        
        self.api = Api(self.api_key)
        self.base = self.api.base(self.base_id)
        
        # Table names
        self.deals_table = self.base.table('Deals')
        self.clients_table = self.base.table('Clients')
        self.payments_table = self.base.table('Payments')
    
    def create_deal(self, deal_data: dict) -> dict:
        """
        Create a new deal in Airtable
        
        Args:
            deal_data: Deal information
            
        Returns:
            Created record
        """
        try:
            record = {
                'Client': deal_data.get('client', ''),
                'Supplier': deal_data.get('supplier', ''),
                'Quantity': deal_data.get('quantity', 0),
                'Country': deal_data.get('country', ''),
                'Delivery Date': deal_data.get('delivery_date', ''),
                'Buy Price': deal_data.get('buy_price', 0),
                'Sell Price': deal_data.get('sell_price', 0),
                'Profit': deal_data.get('profit', 0),
                'Price Per Lead': deal_data.get('price_per_lead', 0),
                'Deal Type': deal_data.get('deal_type', ''),
                'Raw Text': deal_data.get('raw_text', ''),
                'Telegram User': deal_data.get('telegram_user', ''),
                'Telegram Group': deal_data.get('telegram_group', ''),
                'Status': 'Active',
                'Created Date': datetime.now().isoformat()
            }
            
            created_record = self.deals_table.create(record)
            logger.info(f"Deal created: {created_record['id']}")
            return created_record
            
        except Exception as e:
            logger.error(f"Error creating deal: {e}")
            raise
    
    def create_client(self, client_data: dict) -> dict:
        """
        Create a new client/supplier in Airtable
        
        Args:
            client_data: Client information
            
        Returns:
            Created record
        """
        try:
            record = {
                'Name': client_data.get('name', ''),
                'Type': client_data.get('type', ''),
                'Telegram User': client_data.get('telegram_user', ''),
                'Added Date': client_data.get('added_date', datetime.now().isoformat()),
                'Total Deals': 0,
                'Total Revenue': 0
            }
            
            created_record = self.clients_table.create(record)
            logger.info(f"Client created: {created_record['id']}")
            return created_record
            
        except Exception as e:
            logger.error(f"Error creating client: {e}")
            raise
    
    def create_payment(self, payment_data: dict) -> dict:
        """
        Record a payment in Airtable
        
        Args:
            payment_data: Payment information
            
        Returns:
            Created record
        """
        try:
            record = {
                'Deal ID': payment_data.get('deal_id', ''),
                'Amount': payment_data.get('amount', 0),
                'Payment Date': payment_data.get('date', datetime.now().isoformat()),
                'Telegram User': payment_data.get('telegram_user', ''),
                'Type': 'Received'
            }
            
            created_record = self.payments_table.create(record)
            logger.info(f"Payment created: {created_record['id']}")
            return created_record
            
        except Exception as e:
            logger.error(f"Error creating payment: {e}")
            raise
    
    def get_all_deals(self, limit: int = 100) -> list:
        """Get all deals"""
        try:
            records = self.deals_table.all(max_records=limit)
            return records
        except Exception as e:
            logger.error(f"Error fetching deals: {e}")
            return []
    
    def get_recent_deals(self, limit: int = 10) -> list:
        """Get recent deals"""
        try:
            records = self.deals_table.all(
                max_records=limit,
                sort=['-Created Date']
            )
            return records
        except Exception as e:
            logger.error(f"Error fetching recent deals: {e}")
            return []
    
    def get_all_clients(self) -> list:
        """Get all clients and suppliers"""
        try:
            records = self.clients_table.all()
            return records
        except Exception as e:
            logger.error(f"Error fetching clients: {e}")
            return []
    
    def get_deal_by_id(self, deal_id: str) -> dict:
        """Get deal by ID"""
        try:
            record = self.deals_table.get(deal_id)
            return record
        except Exception as e:
            logger.error(f"Error fetching deal {deal_id}: {e}")
            return None
    
    def update_deal(self, deal_id: str, fields: dict) -> dict:
        """Update deal"""
        try:
            updated_record = self.deals_table.update(deal_id, fields)
            logger.info(f"Deal updated: {deal_id}")
            return updated_record
        except Exception as e:
            logger.error(f"Error updating deal {deal_id}: {e}")
            raise
    
    def get_statistics(self) -> dict:
        """Calculate general statistics"""
        try:
            deals = self.get_all_deals()
            clients = self.get_all_clients()
            
            total_profit = 0
            total_leads = 0
            total_revenue = 0
            
            for deal in deals:
                fields = deal.get('fields', {})
                total_profit += fields.get('Profit', 0)
                total_leads += fields.get('Quantity', 0)
                total_revenue += fields.get('Sell Price', 0) * fields.get('Quantity', 0)
            
            avg_profit = total_profit / len(deals) if deals else 0
            avg_price_per_lead = total_revenue / total_leads if total_leads > 0 else 0
            
            return {
                'total_deals': len(deals),
                'total_profit': total_profit,
                'total_leads': total_leads,
                'total_clients': len(clients),
                'avg_profit': avg_profit,
                'avg_price_per_lead': avg_price_per_lead
            }
            
        except Exception as e:
            logger.error(f"Error calculating statistics: {e}")
            return {
                'total_deals': 0,
                'total_profit': 0,
                'total_leads': 0,
                'total_clients': 0,
                'avg_profit': 0,
                'avg_price_per_lead': 0
            }
    
    def search_clients(self, query: str) -> list:
        """Search clients by name"""
        try:
            formula = f"SEARCH(LOWER('{query}'), LOWER({{Name}}))"
            records = self.clients_table.all(formula=formula)
            return records
        except Exception as e:
            logger.error(f"Error searching clients: {e}")
            return []
